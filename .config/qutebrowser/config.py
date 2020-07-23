# Documentation:
#   qute://help/configuring.html
#   qute://help/settings.html

# I'm a tab maniac, often leaving 50-100+ tabs open when I close my browser. You know, for later reading.
# This is basically a must.
config.set('auto_save.session', True);
config.set('session.lazy_restore', True);

# Which cookies to accept.
# With QtWebEngine, this setting also controls other features with tracking capabilities similar to those of cookies; including IndexedDB, DOM storage, filesystem API, service workers, and AppCache. Note that with QtWebKit, only `all` and `never` are supported as per-domain values. Setting `no-3rdparty` or `no- unknown-3rdparty` per-domain on QtWebKit will have the same effect as `all`.
# Valid values:
#   - all: Accept all cookies.
#   - no-3rdparty: Accept cookies from the same origin only. This is known to break some sites, such as GMail.
#   - no-unknown-3rdparty: Accept cookies from the same origin only, unless a cookie is already set for the domain. On QtWebEngine, this is the same as no-3rdparty.
#   - never: Don't accept cookies at all.
config.set('content.cookies.accept', 'all', 'chrome-devtools://*')
config.set('content.cookies.accept', 'all', 'devtools://*')

# User agent to send.
# The following placeholders are defined:
#   - `{os_info}`: Something like "X11; Linux x86_64".
#   - `{webkit_version}`: The underlying WebKit version (set to a fixed value with QtWebEngine).
#   - `{qt_key}`: "Qt" for QtWebKit, "QtWebEngine" for QtWebEngine.
#   - `{qt_version}`: The underlying Qt version.
#   - `{upstream_browser_key}`: "Version" for QtWebKit, "Chrome" for QtWebEngine.
#   - `{upstream_browser_version}`: The corresponding Safari/Chrome version.
#   - `{qutebrowser_version}`: The currently running qutebrowser version. The default value is equal to the unchanged user agent of QtWebKit/QtWebEngine. Note that the value read from JavaScript is always the global value. With QtWebEngine between 5.12 and 5.14 (inclusive), changing the value exposed to JavaScript requires a restart.
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/{webkit_version} (KHTML, like Gecko) {upstream_browser_key}/{upstream_browser_version} Safari/{webkit_version}', 'https://web.whatsapp.com/')
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}; rv:71.0) Gecko/20100101 Firefox/71.0', 'https://accounts.google.com/*')
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99 Safari/537.36', 'https://*.slack.com/*')
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}; rv:71.0) Gecko/20100101 Firefox/71.0', 'https://docs.google.com/*')
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}; rv:71.0) Gecko/20100101 Firefox/71.0', 'https://drive.google.com/*')

# Load images automatically in web pages.
config.set('content.images', True, 'chrome-devtools://*')
config.set('content.images', True, 'devtools://*')

# Enable JavaScript.
config.set('content.javascript.enabled', True, 'chrome-devtools://*')
config.set('content.javascript.enabled', True, 'devtools://*')
config.set('content.javascript.enabled', True, 'chrome://*/*')
config.set('content.javascript.enabled', True, 'qute://*/*')