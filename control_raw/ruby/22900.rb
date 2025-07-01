def notify(callback_method, *data)
    # TODO throw error here ?
    return unless node.persistent?

    msg = Messages::Notification.new :method  => callback_method,
                                     :args    => data,
                                     :headers => @node.message_headers

    # TODO surround w/ begin/rescue block,
    # raise RJR::ConnectionError on socket errors
    @node.send_msg msg.to_s, @connection
  end