var photo = document.getElementById('photo');

Webcam.attach('#photo');

Webcam.set({
    image_format: 'jpeg',
    jpeg_quality: 90
});

function take_snapshot() {
    Webcam.snap(function(data_uri) {
        Webcam.upload(data_uri, '/webcam', function (code, text) {
            window.location.href = text;
        });
    });
}

document.getElementById("upload-input").onchange = function() {
    document.getElementById("upload-form").submit();
};

document.getElementById("camera-button").onclick = take_snapshot;
