def build_fake_sms(mobile, code, company)
      {
        'sid'               => SecureRandom.uuid,
        'mobile'            => mobile,
        'send_time'         => Time.zone.now,
        'text'              => "您的验证码是#{code}。如非本人操作，请忽略本短信【#{company}】",
        'send_status'       => 'SUCCESS',
        'report_status'     => 'UNKNOWN',
        'fee'               => 1,
        'user_receive_time' => nil,
        'error_msg'         => nil
      }
    end