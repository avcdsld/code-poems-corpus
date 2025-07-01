def from_df(cls, ratings:DataFrame, valid_pct:float=0.2, user_name:Optional[str]=None, item_name:Optional[str]=None,
                rating_name:Optional[str]=None, test:DataFrame=None, seed:int=None, path:PathOrStr='.', bs:int=64, 
                val_bs:int=None, num_workers:int=defaults.cpus, dl_tfms:Optional[Collection[Callable]]=None, 
                device:torch.device=None, collate_fn:Callable=data_collate, no_check:bool=False) -> 'CollabDataBunch':
        "Create a `DataBunch` suitable for collaborative filtering from `ratings`."
        user_name   = ifnone(user_name,  ratings.columns[0])
        item_name   = ifnone(item_name,  ratings.columns[1])
        rating_name = ifnone(rating_name,ratings.columns[2])
        cat_names = [user_name,item_name]
        src = (CollabList.from_df(ratings, cat_names=cat_names, procs=Categorify)
               .split_by_rand_pct(valid_pct=valid_pct, seed=seed).label_from_df(cols=rating_name))
        if test is not None: src.add_test(CollabList.from_df(test, cat_names=cat_names))
        return src.databunch(path=path, bs=bs, val_bs=val_bs, num_workers=num_workers, device=device, 
                             collate_fn=collate_fn, no_check=no_check)