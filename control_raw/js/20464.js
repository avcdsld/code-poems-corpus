function configureValues (track) {
  return _.assign(
    {
      td_version: function () {
        return version
      },
      td_client_id: function () {
        return track.uuid
      },
      td_charset: function () {
        return (document.characterSet || document.charset || '-').toLowerCase()
      },
      td_language: function () {
        var nav = window.navigator
        return (
          (nav && (nav.language || nav.browserLanguage)) ||
          '-'
        ).toLowerCase()
      },
      td_color: function () {
        return window.screen ? window.screen.colorDepth + '-bit' : '-'
      },
      td_screen: function () {
        return window.screen
          ? window.screen.width + 'x' + window.screen.height
          : '-'
      },
      td_viewport: function () {
        var clientHeight =
          document.documentElement && document.documentElement.clientHeight
        var clientWidth =
          document.documentElement && document.documentElement.clientWidth
        var innerHeight = window.innerHeight
        var innerWidth = window.innerWidth
        var height = clientHeight < innerHeight ? innerHeight : clientHeight
        var width = clientWidth < innerWidth ? innerWidth : clientWidth
        return width + 'x' + height
      },
      td_title: function () {
        return document.title
      },
      td_description: function () {
        return getMeta('description')
      },
      td_url: function () {
        return !document.location || !document.location.href
          ? ''
          : document.location.href.split('#')[0]
      },
      td_user_agent: function () {
        return window.navigator.userAgent
      },
      td_platform: function () {
        return window.navigator.platform
      },
      td_host: function () {
        return document.location.host
      },
      td_path: function () {
        return document.location.pathname
      },
      td_referrer: function () {
        return document.referrer
      },
      td_ip: function () {
        return 'td_ip'
      },
      td_browser: function () {
        return 'td_browser'
      },
      td_browser_version: function () {
        return 'td_browser_version'
      },
      td_os: function () {
        return 'td_os'
      },
      td_os_version: function () {
        return 'td_os_version'
      }
    },
    track.values
  )
}