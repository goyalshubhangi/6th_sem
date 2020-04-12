  #!/usr/bin/env python
    # coding: utf-8
    
    import numpy as np
    import sklearn as skl
    import pandas as pd
    from sklearn import preprocessing
    file=pd.read_csv('wine.csv')
    file
    
    data=file.values
    print('wine',data[:,1].mean())
    print('wine',data[:,1].std())
    print('Alcohol',data[:,2].mean())
    print('Alcohol',data[:,2].std())
    print('malic acid',data[:,3].mean())
    print('malic acid',data[:,3].std())
    print('ash',data[:,4].mean())
    print('ash',data[:,4].std())
    print('acl',data[:,5].mean())
    print('acl',data[:,5].std())
    print('mg',data[:,6].mean())
    print('mg',data[:,6].std())
    print('phenol',data[:,7].mean())
    print('phenol',data[:,7].std())
    print('flavanoid',data[:,8].mean())
    print('flavanoid',data[:,8].std())
    print('nonfla. phenol',data[:,9].mean())
    print('nonfla. phenol',data[:,9].std())
    print('proanth',data[:,10].mean())
    print('proanth',data[:,10].std())
    print('color.int',data[:,11].mean())
    print('color.int',data[:,11].std())
    print('hue',data[:,12].mean())
    print('hue',data[:,12].std())
    print('OD',data[:,13].mean())
    print('OD',data[:,13].std())
    print('proline',data[:,-1].mean())
    print('proline',data[:,-1].std())
    
    a=data[:,1]
    b=data[:,2]
    c=data[:,3]
    d=data[:,4]
    e=data[:,5]
    f=data[:,6]
    g=data[:,7]
    h=data[:,8]
    i=data[:,9]
    j=data[:,10]
    k=data[:,11]
    l=data[:,12]
    m=data[:,13]
    n=data[:,-1]
    
    scaled_a=preprocessing.scale(a)
    scaled_b=preprocessing.scale(b)
    scaled_c=preprocessing.scale(c)
    scaled_d=preprocessing.scale(d)
    scaled_e=preprocessing.scale(e)
    scaled_f=preprocessing.scale(f)
    scaled_g=preprocessing.scale(g)
    scaled_h=preprocessing.scale(h)
    scaled_i=preprocessing.scale(i)
    scaled_j=preprocessing.scale(j)
    scaled_k=preprocessing.scale(k)
    scaled_l=preprocessing.scale(l)
    scaled_m=preprocessing.scale(m)
    scaled_n=preprocessing.scale(n)
    
    print('Standardized wine Mean',int(scaled_a.mean()))
    print('Standardized wine Standard Deviation',scaled_a.std())
    print('Standardized proline Mean',int(scaled_b.mean()))
    print('Standardized proline Standard Deviation',scaled_b.std())
    print('Standardized malic acid Mean',int(scaled_c.mean()))
    print('Standardized malic acid Standard Deviation',scaled_c.std())
    print('Standardized ash Mean',int(scaled_d.mean()))
    print('Standardized ash Standard Deviation',scaled_d.std())
    print('Standardized acl Mean',int(scaled_e.mean()))
    print('Standardized acl Standard Deviation',scaled_e.std())
    print('Standardized mg Mean',int(scaled_f.mean()))
    print('Standardized mg Standard Deviation',scaled_f.std())
    print('Standardized phenol Mean',int(scaled_g.mean()))
    print('Standardized phenol Standard Deviation',scaled_g.std())
    print('Standardized flavanoid Mean',int(scaled_h.mean()))
    print('Standardized flavanoid Standard Deviation',scaled_h.std())
    print('Standardized nonfla. phenol Mean',int(scaled_i.mean()))
    print('Standardized nonfla. phenol Standard Deviation',scaled_i.std())
    print('Standardized proanth Mean',int(scaled_j.mean()))
    print('Standardized proanth Standard Deviation',scaled_j.std())
    print('Standardized color.int Mean',int(scaled_k.mean()))
    print('Standardized color.int Standard Deviation',scaled_k.std())
    print('Standardized hue Mean',int(scaled_l.mean()))
    print('Standardized hue Standard Deviation',scaled_l.std())
    print('Standardized OD Mean',int(scaled_m.mean()))
    print('Standardized OD Standard Deviation',scaled_m.std())
    print('Standardized proline Mean',int(scaled_n.mean()))
    print('Standardized proline Standard Deviation',scaled_n.std())
        