from appium import webdriver


def before_scenario(context, scenario):
    config = context.config.userdata
    context.caps = __ios(config) if config['os'] == 'ios' else __android(config)
    context.os = context.caps['platformName']
    context.driver = webdriver.Remote('http://localhost:4723/wd/hub', context.caps)


def __android(config):
    return {
        'platformName': 'Android',
        'platformVersion': '7.1.1',
        'deviceName': 'Pixel API 25',
        'app': '/Users/PATHTOFOLDER'
               '/accessLabelBug/build/android/bin/accessLabelBug.apk',
        'appPackage': 'com.jm.accessLabelBug',
        'appActivity': '.AccesslabelbugActivity',
        'automationName': 'uiautomator2',
    }


def __ios(config):
    return {
        'app':
            '/Users/PATHTOFOLDER/accessLabelBug/build/iphone/build/Products'
            '/Debug-iphonesimulator/accessLabelBug.app',
        'platformName': 'iOS',
        'platformVersion': '12.0',
        'deviceName': 'iPad (5th generation)',
        # 'autoAcceptAlerts': True
    }

