def beatExtraction(st_features, win_len, PLOT=False):
    """
    This function extracts an estimate of the beat rate for a musical signal.
    ARGUMENTS:
     - st_features:     a numpy array (n_feats x numOfShortTermWindows)
     - win_len:        window size in seconds
    RETURNS:
     - BPM:            estimates of beats per minute
     - Ratio:          a confidence measure
    """

    # Features that are related to the beat tracking task:
    toWatch = [0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

    max_beat_time = int(round(2.0 / win_len))
    hist_all = numpy.zeros((max_beat_time,))
    for ii, i in enumerate(toWatch):                                        # for each feature
        DifThres = 2.0 * (numpy.abs(st_features[i, 0:-1] - st_features[i, 1::])).mean()    # dif threshold (3 x Mean of Difs)
        if DifThres<=0:
            DifThres = 0.0000000000000001        
        [pos1, _] = utilities.peakdet(st_features[i, :], DifThres)           # detect local maxima
        posDifs = []                                                        # compute histograms of local maxima changes
        for j in range(len(pos1)-1):
            posDifs.append(pos1[j+1]-pos1[j])
        [hist_times, HistEdges] = numpy.histogram(posDifs, numpy.arange(0.5, max_beat_time + 1.5))
        hist_centers = (HistEdges[0:-1] + HistEdges[1::]) / 2.0
        hist_times = hist_times.astype(float) / st_features.shape[1]
        hist_all += hist_times
        if PLOT:
            plt.subplot(9, 2, ii + 1)
            plt.plot(st_features[i, :], 'k')
            for k in pos1:
                plt.plot(k, st_features[i, k], 'k*')
            f1 = plt.gca()
            f1.axes.get_xaxis().set_ticks([])
            f1.axes.get_yaxis().set_ticks([])

    if PLOT:
        plt.show(block=False)
        plt.figure()

    # Get beat as the argmax of the agregated histogram:
    I = numpy.argmax(hist_all)
    bpms = 60 / (hist_centers * win_len)
    BPM = bpms[I]
    # ... and the beat ratio:
    Ratio = hist_all[I] / hist_all.sum()

    if PLOT:
        # filter out >500 beats from plotting:
        hist_all = hist_all[bpms < 500]
        bpms = bpms[bpms < 500]

        plt.plot(bpms, hist_all, 'k')
        plt.xlabel('Beats per minute')
        plt.ylabel('Freq Count')
        plt.show(block=True)

    return BPM, Ratio