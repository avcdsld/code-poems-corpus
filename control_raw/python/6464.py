def deaggregate_record(decoded_data):
    '''Given a Kinesis record data that is decoded, deaggregate if it was packed using the
    Kinesis Producer Library into individual records.  This method will be a no-op for any
    records that are not aggregated (but will still return them).
    
    decoded_data - the base64 decoded data that comprises either the KPL aggregated data, or the Kinesis payload directly.    
    return value - A list of deaggregated Kinesis record payloads (if the data is not aggregated, we just return a list with the payload alone) 
    '''
    
    is_aggregated = True
    
    #Verify the magic header
    data_magic = None
    if(len(decoded_data) >= len(aws_kinesis_agg.MAGIC)):
        data_magic = decoded_data[:len(aws_kinesis_agg.MAGIC)]
    else:
        print("Not aggregated") 
        is_aggregated = False
    
    decoded_data_no_magic = decoded_data[len(aws_kinesis_agg.MAGIC):]
    
    if aws_kinesis_agg.MAGIC != data_magic or len(decoded_data_no_magic) <= aws_kinesis_agg.DIGEST_SIZE:
        is_aggregated = False
        
    if is_aggregated:            
        
        #verify the MD5 digest
        message_digest = decoded_data_no_magic[-aws_kinesis_agg.DIGEST_SIZE:]
        message_data = decoded_data_no_magic[:-aws_kinesis_agg.DIGEST_SIZE]
        
        md5_calc = md5.new()
        md5_calc.update(message_data)
        calculated_digest = md5_calc.digest()
        
        if message_digest != calculated_digest:            
            return [decoded_data]            
        else:                            
            #Extract the protobuf message
            try:    
                ar = kpl_pb2.AggregatedRecord()
                ar.ParseFromString(message_data)
                
                return [mr.data for mr in ar.records]
            except BaseException as e:
                raise e                   
    else:
        return [decoded_data]