def send_local_content
        response.headers['Accept-Ranges'] = 'bytes'
        if request.head?
          local_content_head
        elsif request.headers['Range']
          send_range_for_local_file
        else
          send_local_file_contents
        end
      end