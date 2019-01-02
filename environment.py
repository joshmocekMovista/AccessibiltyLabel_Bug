from appium import webdriver


def before_scenario(context, scenario):
    config = context.config.userdata
    caps = __ios(config) if config['os'] == 'ios' else __android(config)
    context.os = caps['platformName']
    context.driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)


def __android(config):
    return {
        'platformName': 'Android',
        'platformVersion': '7.1.1',
        'deviceName': 'Pixel API 25',
        'app': '/YOURPATHTOAPK/Appcelerator_Studio_Workspace'
               '/accessLabelBug/build/android/bin/accessLabelBug.apk',
        'appPackage': 'com.jm.accessLabelBug',
        'appActivity': '.AccesslabelbugActivity',
        'newCommandTimeout': '2',
        # 'autoGrantPermissions': True
    }


def __ios(config):
    return {
        'app':
            '/YOURPATH/Appcelerator_Studio_Workspace/accessLabelBug/build/iphone/build/Products'
            '/Debug-iphonesimulator/accessLabelBug.app',
        'platformName': 'iOS',
        'platformVersion': '12.0',
        'deviceName': 'iPad (5th generation)',
        # 'autoAcceptAlerts': True
    }
