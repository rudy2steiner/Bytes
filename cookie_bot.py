from urllib import request
from urllib import parse
from http import cookiejar
from urllib import error
import json
# https://passport.aliyun.com/newlogin/login.do?appName=aliyun&fromSite=6&_bx-v=2.0.31

if __name__ == '__main__':
    login_url = 'https://passport.aliyun.com/newlogin/login.do?appName=aliyun&fromSite=6&_bx-v=2.0.31'
    user_agent = r'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36'
    cookie = cookiejar.CookieJar()
    cookie_support = request.HTTPCookieProcessor(cookie)
    opener = request.build_opener(cookie_support)

    for item in cookie:
         print('Name = %s' % item.name)
         print('Value = %s' % item.value)

    headers = {'User-Agent': user_agent, 'Connection': 'keep-alive','Content-Type': 'application/x-www-form-urlencoded' }
    loginId = 'rudycto'
    passwd = '1982a4f4ca534f35b3e7f3c76bd11eb84e4075e32b4a4baa98d66ae8b77cd009f8dd7749647040c17f396e96e409ae77578f0bfb99558c27d3d9203f40476d8f2f0809cf76848dc7629cbd43f3a7a0466bf2ebaf9577ad5f076f1a9ced5d27d32d28f4464bb8fc6c29c82ada586851b2884938092ed5b40a8b419f9cda2f58aa'
    post_data = 'loginId={}&password2={}&keepLogin=false&ua=140%23xAfdP5L8zzWmdQo2mZ5QfpSogB9KQe766lqeCVyj%2FLgNnCUuXCKWFUxd4LgAzINyrGeDNtAz9wVNmcMuWNS80RRJ71B3IAXPG3hqzznTlq2q1KrzzZDaiHEtlzzx2DD3VthqzFHOHMBZlVDCzPrSIXV%2FtFzx2DccdQsHzjbs2A5tl0zxzfbiwevqLz%2BxQDrWd6GzzFd12CGTlsbxFPdGdzsCOSvZrI7ZbIE3r6FIp6PUOvBkc9gfT4qyUEk6%2BJB%2BT1J2Og65UMdwCGmKPxdjYHAJz%2B4YkRUlcvu0plHSNs66OpSQAc004SlNWFA9lOBrmM9XSMJdnht6oL31hkqcN0eEqsyzm9Pw9iEqM1b%2B%2BYgV4Tx34leoFkOxzXtIRiz%2BtKqy1LgfJRG5cR26%2BppLB2bIMSnhwRu0crUwEuIL6ykqMyWBDTA9PmdB5C2SaCVNiUJd0%2F4jmEhahEs9AKvFMekdlEt0%2F7p8sBHILirgsXYYsMVtOGbk7Ro6QUvg4cL5yJIeRnPgVu9lrMD6cp5Qt7ICKvEbLOqk5bKEpchdpTZrTmZJ9DT48pCOKb%2BtdlFGYS%2Fwsa8VcRTLGY9E9BJdrwcwsiaubEsZXnuyOnGptoRzgFsOkI3XpaxiVwAKjqTpvE8ozawdSn4fjdG5LKau%2FjvaBFF3dQm9k6Y%2FstbTMBVeayuH2RsyRkRZuN5W4tvGufp4zDNlwYKF4YpV0Mb74A85AfoNdPBjsY11V3i40EiL8Httw%2BhnXIx7z%2BHigSwSOoQyzql5CvvT4ybhrqGW7%2FQKlVfoc8GTYAYtwNCcyLb623KdMewT9ZS8sP06m%2B3BTcIPZDwUaqhx0qCZrUWZDP0pNnFyOADgKbvLOaAxecmYVCUD3FFewhHE6T%2BAxk8DxN%2Fl78i%2Frh3vK%2BN8SFrcEn4km8s%2BHr%2Bb8QviEUsqPF14MXVnSFyZdIeMMaPlNU2D6%2F9chk2TRzyuZchduzMsBht9dJDOSLzkaFM9rVt5BjQzP1iaEMirk2NVUedllIObxjjRxY7yeZ3yd%2B2s592JBpX7zDX3LFA7yC%2B%2Fz1KKlSLdAS2Js%2BxoD%2FzRac3xUXHkHiI9fl6SL9tFdlpyDxJGLVLnt20zH2Q66%2BDlb%2BDBKBxooSIoIbpVcqZtiUvPOREUyVvTYGVbFGgW1jzDrPh7VpP4Oh7mFy9po0s7HOSGM5PWW1FBivPbSKTx3yM78jqE%2FDuzaKmQg4y9x6mGCg06uNmP9toR5tsjGYW7bOaODdWX8MCXsuc%2BzicxLbX3LGk9y6onLNj0q%2FWcGPFY7XnwMliUAXCPUkLOWBqG94VJu7piFl%2FdsshKz9Kz%2BR924vmOC6Nbwo6EYRlsrhbHqzYnGHK1tj7YrqT9B8E77O3f%2FGPgpSF8xP%2FTZwPGF47sZLxwjFfwtrrtk%2FYYLq30Far0Y05I0uScKf1WTf21OmblG18Dm9C5AuNh9V%2F1pJUQwkESczN28s%2FeOiFla2rSFZg4Pu21vQaQFjZEpepKHnLnQ7t93%2BD3i5A1sat3Awtpte0YrMHv4p3Aj%2FVVhu2giz2NBm9p7%2BLBKeoR7tWKu3YMa28m5r45OQTRRSwFuuNDau0yCKrZH9WTJy96Z84eHClfDjp4tTKQ0iQVdCyoXF%2Bxy%2BA3rZN%2BTENHuGIpYN8duwUduov84yFVCNnUeZyHnbWbzxPPkly1dudwiL44vjWQhuFiBs9jd7AYrx0mXr7%2BuUnvZT1JSgVFxgxUFVWaqz10DaOpRpY3pktqcJnKwiOcPT6Ybs0FbdxUApeuIQvt6SSQiOPTffKR9Rw7WuQW5oeEu4QPzWthd4rOxEr%3D&umidGetStatusVal=255&screenPixel=1792x1120&navlanguage=zh-CN&navUserAgent=Mozilla%2F5.0%20%28Macintosh%3B%20Intel%20Mac%20OS%20X%2010_15_7%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F89.0.4389.82%20Safari%2F537.36&navPlatform=MacIntel&appName=aliyun&appEntrance=aliyun&_csrf_token=1wptLPrJvDugkkU5mED0S4&umidToken=cd13b5df7d8ed297672c7f30836425d1c060d314&isMobile=false&lang=zh_CN&returnUrl=https%3A%2F%2Faccount.aliyun.com%2Flogin%2Flogin_aliyun.htm%3Foauth_callback%3Dhttps%253A%252F%252Fhomenew.console.aliyun.com%252Fhome%252Fdashboard%252FOperation%253Faccounttraceid%253D4e2452d59887496ca76ebdbdb33512dccuci&hsiz=1f5255d92ad855070161ab532175810b&fromSite=6&bizParams=&bx-ua=210!bER0HzcqzzPOGBwurPVoUULCnKR+mTPw1vfyj9t4bP2+C2fFDVFwg6koG/jPQztbLUviHqVxj4eS5EwyzBXwq6LVENgVRPtKLEJoHMi2zhJXLxyyFrzwW6GVHdj4Dzb7LaRKrleWzWIQL6twgEYveFuXLzdJiioijXMKdm/XpWeQx6BtZQ9rtqpo/bnrATild62OqfTPSlqTrxM2qg4rYtnVr6TgcAFNjQf8wam7SJdqlWeiGXBG28Wm+mH20OgZKmdipf+ppAtTBRmi0oEdFdkSv0+zERbv0Yxtxfy99nlZiKMtEYbQpaTolmTUvIZEQg628aWs/Lf0vuciZXcBSkWz+0GgAu3kZ6QK8ar+FujgDL/OG54k9tIC4YrvTrzdkXWi70kuVzmXLSjyhGYzOxcalMbDSB1MLlrxsQDGRkV7wC7pDizzlEgwP7WCiPbzLUqfzot+zzWoL9hz7DUzzx/kxRRPizYzZkE70ywIuWjob6MxlZz7zm/JzRR4DzbzZkExXSfIF6vndLzzlEg7zm/JzzWalBwHE5HYddg7tfgFwd2SbFYPbzC25Q/RB8YCwP314FSRbBgFwCj1BKVqWzMa4M+RBvDawBcj1FXU4Bgawb9bBKFabPTo4EwRBkJmwzct4YSRw3X27CyA9eN6WzIDEC0Sxvza/B314Fawb7b2wM9WBKzabzMF4DnWr7zawac1kgFgbzEFfCmdBgbPwxDWPDl1VqyTgac14gawbzgFwC5bBgFPbzB24MnRBIMNwzCXX//OYA7q/DmqBgSGbzMF4DntrBgPwP3W4YSK7N1mLzE8kl4RGqJ7x6od1FUxVBmJY9vCXXIMpyjUnv/sXpxPXHINe0wj9oNZ0eqyWB2vBuCX3uQ+SZckLdI0Jk9NcaYxE5eIdjE1E12muR2g9rf56Mp8fQe6hOVzTNFQwBqNLQHh1ncUqVHMCwQtMCcxKJzC+sJWePOmv3J61U+XSWeHLgFKJdq6qchVtNou+nH7bD8lcEuqTYVCsV3DRDafBXl+KEPKlGhq8L3D689zqRo2+FpaJ6PG+JdGBG1xpVi7Qwhk5Rq4eAx1obqS8PCVHFYWx9Ka41BUTnl/24N1RH+qCbALMVCTlLuqJqJUJmp9Pfokwh8wf3j1k8ed0uGowUROSctUMqIlBJsRwbiaR/h+zQleGtmOuqWqr8vAQDRPXTP2nWfZ1cy0ryclX7vKB2vaezgDO61CBPSjF92VkPv7daOA5671DUutUOY1k0YfPH7y1KYD7l1oq/8Hx3ElQWJA8bATdmQmqeZ33427UhLqIeQHOze7QMD4gPlrCRsucMn2cKtQZ+gaqs5ZowlNnPQo1kmJYyjG1ZNYv2+UutHXAg9tuCa/L1sl2IYeMH3tHfWEa1WCFXCV58pJGyhbZ7NiUOtMIwKRPk1ATOpOnys3/PMQ9u0zHhEKsExn90GxSxPszyjW2Ow1hetUQL60YeKXq3D4l35EZLdBwhVaWW+iHDsVK2CA46iowtLQzl47pHchK0p6G+DD85xA0T45R7ai2FJpBfpXohJ/zKi4FJut/aEG1JqtO4DQY0WHC8DyCUk9/IbD+xcbm3QrzPVxlD7eT9T1IpEeMVmceKjVDMEL2SAy1LwOW56tT4gGDLUvmB7JCG13mCoXMwcH/l9M+hbr+37rNffBoqGciV2+scifLtX0K4TDzCgyaY0/rxqpP277dwZ3Nv7wQFLahG4OKsj+A+fXeOMPr0PLkJFVk0knAj6MwAAUUbL7a2pc3Kj9LgcPQT+NRpu00ayQtsaiurAvL3MYGIscIy+aMRS5ZVRfoqdA+AQgDpXncgbXfNSuACL7xlAVcEN0+w3MW2ySD/zyUJzaBTqvS6HbZcDd2S/Y699/S1Eim7s3u4xD+508X/Xnir6R869YY+EpYJ/i5NNb2jp47WWGTkWeMYsGYtZckIEdu0TYvi871AL2rfZ8tq/sejkQiXJSfP==&bx-umidtoken=T2gA2R1bA7mH1uenIYwHUyj6EapzHkzMvm-Y7BojXOA4sMB8UmDJy3Ajb52lggw1tvk='
    body = str.format(post_data, loginId, passwd)
    encode_post_data = body.encode('utf-8')
    req = request.Request(url=login_url, data=encode_post_data, headers=headers)
    req2 = request.Request(url= 'https://domain.console.aliyun.com/#/booklist', headers= headers)
    print(body)
    print(req)
    try:
        response = opener.open(req)
        html1 = response.read().decode('utf-8')
        resp2 = opener.open(req2)
        html2 = resp2.read().decode('utf-8')
        print('r1:'+html1)
        print('r2:'+html2)
    except error.URLError as e:
        print(e)
