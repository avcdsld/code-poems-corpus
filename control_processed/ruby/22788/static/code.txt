def admin_update_vendor_status
      vendor = Vendor.find(params[:id])
      vendor.status = params[:status]
      render :json => vendor.save
    end