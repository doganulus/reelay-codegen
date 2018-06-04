#include <boost/icl/interval.hpp>
#include <boost/icl/interval_set.hpp>

typedef boost::icl::interval<int> interval;
typedef boost::icl::interval_set<int> timed_set;

timed_set& update_timed_since(timed_set& tstate, bool p1, bool p2, int upper, int now){
   
    if(p2){
        tstate = tstate.add(now) - interval::open(0, now-upper);
    } else if(p1 and !boost::icl::is_empty(tstate)){
        tstate = tstate - interval::open(0, now-upper);
    } else {
        tstate = timed_set();
    }

    return tstate;
}

timed_set& update_timed_since_unbounded(timed_set& tstate,  bool p1, bool p2, int lower, int now){
   
    if(p2){
        tstate = tstate.add(now);
    } else if(!p1 or boost::icl::is_empty(tstate)){
        tstate = timed_set();
    }

    if(!boost::icl::is_empty(tstate - interval::left_open(now-lower, now))){
        tstate = tstate + interval::left_open(0, now-lower);
    }

    return tstate;
}

bool output_timed_since(timed_set& tstate, int lower, int now){
    return !boost::icl::is_empty(tstate - interval::left_open(now-lower, now));
}

bool output_timed_since_unbounded(timed_set& tstate, int now){
    return !boost::icl::is_empty(tstate);
}

