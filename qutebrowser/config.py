config.load_autoconfig()
c.content.cookies.accept = 'no-unknown-3rdparty'
c.qt.low_end_device_mode = 'always'
c.scrolling.bar = 'overlay'
c.search.ignore_case = 'always'
c.statusbar.position = 'top'
c.statusbar.show = 'in-mode'
c.statusbar.widgets = ['keypress', 'url', 'scroll', 'tabs', 'progress']
c.tabs.background = True
c.tabs.favicons.scale = 1.5
c.tabs.favicons.show = 'always'
c.tabs.indicator.width = 0
c.tabs.max_width = 50
c.tabs.padding = {'top': 5, 'bottom': 5, 'left': 5, 'right': 5}
c.tabs.position = 'left'
c.tabs.show = 'switching'
c.tabs.show_switching_delay = 1000
c.tabs.title.format = ''
c.tabs.tooltips = False
c.tabs.width =  30
c.url.start_pages = ['file:///home/mia/ProgrammingProjects/Homepage/index.html']
c.window.hide_decoration = True
config.bind('<Ctrl-1>', 'tab-focus 1')
config.bind('<Ctrl-2>', 'tab-focus 2')
config.bind('<Ctrl-3>', 'tab-focus 3')
config.bind('<Ctrl-4>', 'tab-focus 4')
config.bind('<Ctrl-5>', 'tab-focus 5')
config.bind('<Ctrl-6>', 'tab-focus 6')
config.bind('<Ctrl-7>', 'tab-focus 7')
config.bind('<Ctrl-8>', 'tab-focus 8')
config.bind('<Ctrl-9>', 'tab-focus -1')
config.bind('<Ctrl-m>', 'tab-mute')
config.source('qutewal.py')
