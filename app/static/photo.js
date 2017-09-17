var photo = document.getElementById('photo');

Webcam.set({
    width: photo.offsetWidth,
    height: photo.offsetHeight,
    image_format: 'jpeg',
    jpeg_quality: 90
});

Webcam.attach('#photo');

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
