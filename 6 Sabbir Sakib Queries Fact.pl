like(sakib,cricket).
like(sakib,football).
like(sakib,rugby).

like(riad,football).
like(riad,rugby).

like(sabbir,flower).
like(sabbir,custurd).
like(sabbir,fruits).

sabbirlikes(X):- like(X,football).
sakiblikes(Y):- like(sabbir,Y).
