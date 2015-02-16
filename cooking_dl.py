import netrc
import os

import selenium.webdriver
import wget

rc = netrc.netrc()
user, host, password = rc.hosts['coursera-dl']

try:
    os.makedirs(os.path.join('.', 'videos'))
except OSError:
    pass

browser = selenium.webdriver.Firefox()
browser.implicitly_wait(10)
try:
    browser.get('https://www.coursera.org/learn/childnutrition/outline')

    browser.find_element_by_link_text('Log In').click()
    browser.find_element_by_css_selector('div[data-state="login"] #user-modal-email').send_keys(user)
    browser.find_element_by_css_selector('div[data-state="login"] #user-modal-password').send_keys(password)
    browser.find_element_by_css_selector('div[data-state="login"] button[data-js="submit"]').click()

    browser.find_element_by_id('coursera-header-account-popup')

    links = browser.find_elements_by_css_selector('a[href*="learn/childnutrition/lecture"]')
    links = [a.get_attribute('href') for a in links]

    for i, l in enumerate(links):
        print 'Processing', l
        browser.get(l)
        video = browser.find_element_by_tag_name('video')
        video_url = video.get_attribute('src')
        fname = '%05d_%s.mp4' % (i + 1, os.path.basename(l))

        fpath = os.path.join('.', 'videos', fname)
        if not os.path.exists(fpath):
            print 'Saving to %s' % fname
            wget.download(video_url, out=fpath)
            print ''
finally:
    browser.quit()
