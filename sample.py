KB = 1024
MB = 1024 ** 2
GB = 1024 ** 3
TB = 1024 ** 4
SECOND = 1
MINUTE = 60
HOUR = 60 * 60
DAY = 24 * 60 * 60

# 所有填写的文件夹和文件请预先创建好，本程序不会自动创建它们，所有信息没有另外说的都是必填
CONFIG = {
    # log文件输出路径，本程序所有输出都会保存一份在这个log里
    "log_file": "./filter.log",
    # filter的通用设置
    "filter": {
        # 从这个文件夹里读取.torrent，此文件夹应为irssi等工具的保存种子的文件夹
        "source_dir": "./tocheck",
        # 满足filter条件的种子会被转存到这个文件夹，此文件夹应为bt客户端的监控文件夹
        "dest_dir": "./watch",
        # 对于未配置信息的站点r到的种子的行为，默认是接受（即认为是满足条件），如果不要接受请改成"reject"
        "default_behavior": "accept",
    },
    # dic 配置信息，如果不需要刷dic请将分割线1内整段注释掉
    # ========================分割线1=============================
    "dic": {
        # 一个文件夹，保存曾经请求过的api回复，如果不需要可以填None
        "api_cache_dir": "./cache/dic",
        # 关于cookie的填写请参考`README.rss.md`里的描述
        "cookies": {
            "PHPSESSID": "dic_PHPSESSID",
            "session": "dic_session"
        },
        # authkey和torrent_pass请随便复制一个种子的下载链接，里面有
        "authkey": "dic_key",
        "torrent_pass": "dic_pass",
        # filter_config的填写请参考上面的模板FILTER_CONFIG_TEMPLATE和给出的样例
        "filter_config": {
            "name": "dicfilter",
            "banlist": None,
            "whitelist": None,
            "media": None,
            "format": set(["FLAC"]),
            "sizelim": None,
        },
        # 体积在这个区间内时自动使用令牌，样例：100MB-2GB，如果不想使用令牌请填一个非法的区间，比如(0,-1)
        # 注意，即使令牌用完，本脚本依然会继续下载种子，此时等于下黑种，请关注令牌余量
        "token_thresh": (100 * MB, 2 * GB),
        # 自动ban人脚本条件，如果需要对海豚使用该脚本，请取消以下的注释：
        # 填写时，请参考上面的模板AUTOBAN_TEMPLATE和给出的样例
        # "autoban" : {
        #     "ratio" : [
        #         {"count":1, "ratiolim":0.2},
        #     ],
        #     "ignore": {
        #         "min_progress" : 0.3,
        #         "max_time_added" : 36 * HOUR,
        #     },
        # },
    },
    # ========================分割线1=============================
    # red 配置信息，如果不需要刷red请将分割线2内整段注释掉（默认是注释掉的）
    # ========================分割线2=============================
    "red": {
        # 一个文件夹，保存曾经请求过的api回复，如果不需要自动拉黑脚本可以填None
        "api_cache_dir": "./cache/red",
        # cookie/apikey二选一用于鉴权，推荐使用api_key，因为可以缩小一半的api请求间隔限制（10秒5次->10秒10次）
        # 如果非要使用cookie的话，请将cookie取消注释，并将api_key填为None
        # 关于cookie的填写请参考`README.rss.md`里的描述
        # "cookies"       : {
        #     "session": "xxxxxxxxxxxx"
        # },
        # apikey请在red个人设置页面进行设置，记得勾选"Confirm API Key"并保存之后apikey才生效
        "api_key": "red_api",
        # authkey和torrent_pass请随便复制一个种子的下载链接，里面有
        "authkey": "red_key",
        "torrent_pass": "red_pass",
        # filter_config的填写请参考上面的模板FILTER_CONFIG_TEMPLATE和给出的样例
        "filter_config": {
            "name": "redfilter",
            "banlist": None,
            "whitelist": None,
            "media": set(["CD"]),
            "format": None,
            "sizelim": (100 * MB, 1024 * MB)
        },
        # red staff说red规则不允许自动使用token，请不要修改"token_thresh"（修改了也没用）
        "token_thresh": (0, -1),
        # 自动ban人脚本条件，如果需要对red使用该脚本，请取消以下的注释：
        # 填写时，请参考上面的模板AUTOBAN_TEMPLATE和给出的样例
        # "autoban" : {
        #     "ratio" : [
        #         {"count":1, "ratiolim":0.2},
        #     ],
        #     "ignore": {
        #         "min_progress" : 0.3,
        #         "max_time_added" : 36 * HOUR,
        #     },
        # },
    },
    # ========================分割线2=============================
    # ops 配置信息，如果不需要刷ops请将分割线3内整段注释掉（默认是注释掉的）
    # ========================分割线3=============================
    "ops": {
        # 保存曾经请求过的api回复，如果不需要可以填None
        "api_cache_dir": "./cache/ops",
        # cookie/apikey二选一用于鉴权
        # 如果使用cookie的话，请将cookie取消注释，并将api_key填为None
        # 关于cookie的填写请参考`README.rss.md`里的描述
        # "cookies"       : {
        #     "session"   : "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
        # },
        # apikey请在ops个人设置页面进行设置
        "api_key": "ops_api",
        # authkey和torrent_pass请随便复制一个种子的下载链接，里面有
        "authkey": "ops_key",
        "torrent_pass": "ops_pass",
        # filter_config的填写请参考上面的模板FILTER_CONFIG_TEMPLATE和给出的样例
        "filter_config": {
            "name": "opsfilter",
            "banlist": None,
            "whitelist": None,
            "media": None,
            "format": set(["FLAC"]),
            "sizelim": (100 * MB, 1 * GB),
        },
        #     # ops staff说ops规则不允许自动使用token，请不要修改"token_thresh"（修改了也没用）
        #     "token_thresh": (0, -1),
        #     # 自动ban人脚本条件，如果需要对ops使用该脚本，请取消以下的注释：
        #     # 填写时，请参考上面的模板AUTOBAN_TEMPLATE和给出的样例
        #     # "autoban" : {
        #     #     "ratio" : [
        #     #         {"count":1, "ratiolim":0.2},
        #     #     ],
        #     #     "ignore": {
        #     #         "min_progress" : 0.3,
        #     #         "max_time_added" : 36 * HOUR,
        #     #     },
        #     # },
    },
    # ========================分割线4=============================
    # deluge客户端的登陆信息，如果不需要自动ban人脚本可以不填
    "deluge": {
        "ip": "127.0.0.1",
        # 这个端口是deluge api的端口，而不是deluge暴露在外网监听bt连接的端口，在webui上点"connect manager"在host一栏上会显示这个端口
        "port": 12345,
        "username": "xxxxxxxxxxxxxx",
        "password": "xxxxxxxxxxxxxx",
    },
    # requests发送请求的超时时间，不知道是啥的可以不改，单位：秒
    "requests_timeout": 10,
}
