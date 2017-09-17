Webcam.set({
    width: 320,
    height: 240,
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
