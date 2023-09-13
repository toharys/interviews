// input: v - vector of executions time of various test 
//        N - the given time to make test
// output: the longest sub-vector of tests such that their total execution times is the max that less than N

std::vector<int> greedy(int N, std::vector<int> v){
  std::vector<int> res();
  std::sort(v.begin(), v.end());
  int sum = 0, i=0;
  while(i<v.size() && sum<=N){
    sum+=v[i];
    res.push_back(i);
  }
  return res;    
}

std::vector<int> opt_tests(int N, std::vector<int> v){
  std::vector<int> prev_res = grredy(N,v);
  std::vector<int> curr_res = greedy(N,v.del(std::min(prev_res)));
  while( std::sum(curr_res))>std::sum(prev_res) && curr_res.size()>=prev_res.size()){
    prev_res = curr_res;
    curr_res = greedy(N,v.del(std::min(prev_res)));
  }
return prev_res;
}
