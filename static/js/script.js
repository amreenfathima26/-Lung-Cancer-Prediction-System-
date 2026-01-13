const fileInput = document.getElementById('fileInput');
const uploadBox = document.getElementById('uploadBox');
const previewSection = document.getElementById('previewSection');
const previewImage = document.getElementById('previewImage');
const predictBtn = document.getElementById('predictBtn');
const changeImageBtn = document.getElementById('changeImageBtn');
const resultsSection = document.getElementById('resultsSection');
const loading = document.getElementById('loading');
const errorMessage = document.getElementById('errorMessage');
const predictionLabel = document.getElementById('predictionLabel');
const confidenceBadge = document.getElementById('confidenceBadge');
const progressBar = document.getElementById('progressBar');
const predictionList = document.getElementById('predictionList');

let selectedFile = null;

// Click to upload
uploadBox.addEventListener('click', () => {
    fileInput.click();
});

// File input change
fileInput.addEventListener('change', (e) => {
    handleFileSelect(e.target.files[0]);
});

// Drag and drop
uploadBox.addEventListener('dragover', (e) => {
    e.preventDefault();
    uploadBox.classList.add('dragover');
});

uploadBox.addEventListener('dragleave', () => {
    uploadBox.classList.remove('dragover');
});

uploadBox.addEventListener('drop', (e) => {
    e.preventDefault();
    uploadBox.classList.remove('dragover');
    const file = e.dataTransfer.files[0];
    if (file) {
        handleFileSelect(file);
    }
});

function handleFileSelect(file) {
    if (!file) return;

    // Validate file type
    const validTypes = ['image/png', 'image/jpeg', 'image/jpg'];
    if (!validTypes.includes(file.type)) {
        showError('Please upload a valid image file (PNG, JPG, or JPEG)');
        return;
    }

    // Validate file size (16MB)
    if (file.size > 16 * 1024 * 1024) {
        showError('File size exceeds 16MB limit');
        return;
    }

    selectedFile = file;

    // Show preview
    const reader = new FileReader();
    reader.onload = (e) => {
        previewImage.src = e.target.result;
        uploadBox.style.display = 'none';
        previewSection.style.display = 'block';
        resultsSection.style.display = 'none';
        hideError();
    };
    reader.readAsDataURL(file);
}

function showError(message) {
    errorMessage.textContent = message;
    errorMessage.style.display = 'block';
    setTimeout(() => {
        hideError();
    }, 5000);
}

function hideError() {
    errorMessage.style.display = 'none';
}

// Change image button
changeImageBtn.addEventListener('click', () => {
    selectedFile = null;
    uploadBox.style.display = 'block';
    previewSection.style.display = 'none';
    resultsSection.style.display = 'none';
    fileInput.value = '';
    hideError();
});

// Predict button
predictBtn.addEventListener('click', async () => {
    if (!selectedFile) {
        showError('Please select an image first');
        return;
    }

    // Show loading
    loading.style.display = 'block';
    previewSection.style.display = 'none';
    resultsSection.style.display = 'none';
    hideError();

    // Create form data
    const formData = new FormData();
    formData.append('file', selectedFile);

    try {
        const response = await fetch('/predict', {
            method: 'POST',
            body: formData
        });

        const contentType = response.headers.get("content-type");
        if (contentType && contentType.indexOf("application/json") !== -1) {
            const data = await response.json();

            loading.style.display = 'none';

            if (data.error) {
                showError(data.error);
                previewSection.style.display = 'block';
            } else if (data.success) {
                displayResults(data);
            } else {
                showError('An unexpected error occurred');
                previewSection.style.display = 'block';
            }
        } else {
            // Handle non-JSON response (likely HTML error page)
            const text = await response.text();
            loading.style.display = 'none';
            console.error("Server returned non-JSON:", text);
            // Extract title if present
            const match = text.match(/<title>(.*?)<\/title>/i);
            const title = match ? match[1] : "Server Error";
            showError(`Server Error: ${title}. Check console for details.`);
            previewSection.style.display = 'block';
        }

    } catch (error) {
        loading.style.display = 'none';
        showError('Network error: ' + error.message);
        previewSection.style.display = 'block';
    }
});

function displayResults(data) {
    // Update main prediction
    predictionLabel.textContent = data.prediction;
    confidenceBadge.textContent = `${data.confidence}%`;

    // Update progress bar
    progressBar.style.width = `${data.confidence}%`;
    progressBar.textContent = `${data.confidence}%`;

    // Update all predictions
    predictionList.innerHTML = '';

    // Sort predictions by confidence
    const sortedPredictions = Object.entries(data.all_predictions)
        .sort((a, b) => b[1] - a[1]);

    sortedPredictions.forEach(([label, percentage]) => {
        const item = document.createElement('div');
        item.className = 'prediction-item';

        const labelSpan = document.createElement('span');
        labelSpan.className = 'label';
        labelSpan.textContent = label;

        const percentageSpan = document.createElement('span');
        percentageSpan.className = 'percentage';
        percentageSpan.textContent = `${percentage.toFixed(2)}%`;

        item.appendChild(labelSpan);
        item.appendChild(percentageSpan);
        predictionList.appendChild(item);
    });

    // Show results
    resultsSection.style.display = 'block';
    previewSection.style.display = 'block';

    // Scroll to results
    resultsSection.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

