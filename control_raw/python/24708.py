def install(path, user, admin_user, admin_password, admin_email, title, url):
    '''
    Run the initial setup functions for a wordpress install

    path
        path to wordpress install location

    user
        user to run the command as

    admin_user
        Username for the Administrative user for the wordpress install

    admin_password
        Initial Password for the Administrative user for the wordpress install

    admin_email
        Email for the Administrative user for the wordpress install

    title
        Title of the wordpress website for the wordpress install

    url
        Url for the wordpress install

    CLI Example:

    .. code-block:: bash

        salt '*' wordpress.install /var/www/html apache dwallace password123 \
            dwallace@example.com "Daniel's Awesome Blog" https://blog.dwallace.com
    '''
    retcode = __salt__['cmd.retcode']((
        'wp --path={0} core install '
        '--title="{1}" '
        '--admin_user={2} '
        "--admin_password='{3}' "
        '--admin_email={4} '
        '--url={5}'
    ).format(
        path,
        title,
        admin_user,
        admin_password,
        admin_email,
        url
    ), runas=user)

    if retcode == 0:
        return True
    return False