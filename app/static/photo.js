function getParameterByName(name, url) {
    if (!url) url = window.location.href;
    name = name.replace(/[\[\]]/g, "\\$&");
    var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
        results = regex.exec(url);
    if (!results) return null;
    if (!results[2]) return '';
    return decodeURIComponent(results[2].replace(/\+/g, " "));
}

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

console.log(getParameterByName('face_error'));
if (getParameterByName('face_error') == 1) {
		document.getElementById("face-error").show()
}
