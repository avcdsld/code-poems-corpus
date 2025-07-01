def login(self, user, password, exe_path, comm_password=None, **kwargs):
        """
        登陆客户端
        :param user: 账号
        :param password: 明文密码
        :param exe_path: 客户端路径类似 'C:\\中国银河证券双子星3.2\\Binarystar.exe',
            默认 'C:\\中国银河证券双子星3.2\\Binarystar.exe'
        :param comm_password: 通讯密码, 华泰需要，可不设
        :return:
        """
        try:
            self._app = pywinauto.Application().connect(
                path=self._run_exe_path(exe_path), timeout=1
            )
        # pylint: disable=broad-except
        except Exception:
            self._app = pywinauto.Application().start(exe_path)
            is_xiadan = True if "xiadan.exe" in exe_path else False
            # wait login window ready
            while True:
                try:
                    self._app.top_window().Edit1.wait("ready")
                    break
                except RuntimeError:
                    pass

            self._app.top_window().Edit1.type_keys(user)
            self._app.top_window().Edit2.type_keys(password)
            while True:
                self._app.top_window().Edit3.type_keys(
                    self._handle_verify_code(is_xiadan)
                )
                self._app.top_window()["确定" if is_xiadan else "登录"].click()

                # detect login is success or not
                try:
                    self._app.top_window().wait_not("exists visible", 10)
                    break
                # pylint: disable=broad-except
                except Exception:
                    if is_xiadan:
                        self._app.top_window()["确定"].click()

            self._app = pywinauto.Application().connect(
                path=self._run_exe_path(exe_path), timeout=10
            )
        self._close_prompt_windows()
        self._main = self._app.window(title="网上股票交易系统5.0")
        try:
            self._main.child_window(
                control_id=129, class_name="SysTreeView32"
            ).wait("ready", 2)
        # pylint: disable=broad-except
        except Exception:
            self.wait(2)
            self._switch_window_to_normal_mode()