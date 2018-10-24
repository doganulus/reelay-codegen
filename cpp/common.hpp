#include <boost/icl/interval.hpp>
#include <boost/icl/interval_set.hpp>

using namespace boost::icl;

template <class V, class T>
bool lt(V value, T threshold){
    return value < threshold;
}
template <class V, class T>
bool leq(V value, T threshold){
    return value <= threshold;
}
template <class V, class T>
bool gt(V value, T threshold){
    return value > threshold;
}
template <class V, class T>
bool geq(V value, T threshold){
    return value >= threshold;
}


template <typename K, typename V1, typename V2, typename T>
interval_set<V> lt(interval_set<K> current, V1 y1, V2 y2, T threshold){
    if(y1 < )
}