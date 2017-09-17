var pswpElement = document.querySelectorAll('.pswp')[0];

// build items array
var items = [
    {
        src: 'http://localhost:8000/static/img/jolly-toper-1629.jpg!HD.jpg',
        w: 1137,
        h: 1200
    },
    {
        src: 'http://localhost:8000/static/img/the-broken-pitcher-1891.jpg!HD.jpg',
        w: 751,
        h: 1200
    }
];

// define options (if needed)
var options = {
    // optionName: 'option value'
    // for example:
    index: 0 // start at first slide
};

// Initializes and opens PhotoSwipe
var gallery = new PhotoSwipe( pswpElement, PhotoSwipeUI_Default, items, options);
gallery.init();
