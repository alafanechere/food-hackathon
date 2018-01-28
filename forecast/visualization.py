def prediction_profile(df,by,bins=None,range=None):
    """
    Input df should contain :
        df['pred']          actual prediction
        df['pred_min']      lower confidence interval
        df['pred_max']      upper confidence interval
        df['err']           actual error
        df['err_min']       lower error
        df['err_max']       upper error
    """
    if bins is not None:
        if range is None:
            range = df[by].min(),df[by].max()
        bins = np.linspace(*range,bins+1)
        labels = 0.5*(bins[1:]+bins[:-1])
        #print(bins)
        df[by+'_bins'] = pd.cut( df[by], bins, labels=labels ).astype(np.float)
        by = by+'_bins'



    meanpred = df.groupby(by)['pred'].mean()
    meanpred_min = df.groupby(by)['pred_min'].mean()
    meanpred_max = df.groupby(by)['pred_max'].mean()
    unc = 0.5*(meanpred_max-meanpred_min)
    meantrue = df.groupby(by)['price'].mean()
    stdtrue = df.groupby(by)['price'].std()

    mean = df.groupby(by)['err'].mean()
    maxp = df.groupby(by)['err_min'].mean()
    minp = df.groupby(by)['err_max'].mean()

    std = df.groupby(by)['err'].std()

    r2 = 1. - (std/stdtrue)**2

    plt.scatter(meantrue.index,meanpred)
    plt.plot(meanpred,color='red')
    plt.fill_between(mean.index, meanpred - std, meanpred+std, color='red', alpha=0.5)
    plt.show()

    plt.scatter(meantrue.index,meanpred)
    plt.plot(meanpred,color='orange')
    plt.fill_between(meanpred.index, meanpred - unc, meanpred + unc, color='orange', alpha=0.5)

    plt.show()

    plt.plot(r2)
    plt.show()

    plt.plot(minp)
    plt.plot(maxp)
    plt.show()
