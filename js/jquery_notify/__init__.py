from fanstatic import Library, Resource
from js.jquery import jquery

library = Library('jquery_notify', 'resources')

jquery_notify = Resource(library, 'jquery.notify.js', minified='jquery.notify.min.js', depends=[jquery,])