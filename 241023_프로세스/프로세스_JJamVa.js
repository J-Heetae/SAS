function solution(priorities, location) {
  let answer = 0;
  let copy_arr = [...priorities].map((e, i) => ({
    value: e,
    location: i === location ? true : false,
  }));

  while (copy_arr.length > 0) {
    let num = Math.max(...copy_arr.map((e) => e.value));
    if (copy_arr[0].value < num) {
      copy_arr.push(copy_arr.shift());
    } else {
      answer++;
      if (copy_arr[0].location) return answer;
      copy_arr.shift();
    }
  }

  return answer;
}
