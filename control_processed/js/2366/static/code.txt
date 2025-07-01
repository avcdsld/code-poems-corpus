function () {
        // 初始化配置信息
        this._initConfig()

        // 初始化 DOM
        this._initDom()

        // 封装 command API
        this._initCommand()

        // 封装 selection range API
        this._initSelectionAPI()

        // 添加 text
        this._initText()

        // 初始化菜单
        this._initMenus()

        // 添加 图片上传
        this._initUploadImg()

        // 初始化选区，将光标定位到内容尾部
        this.initSelection(true)

        // 绑定事件
        this._bindEvent()
    }