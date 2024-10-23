function solution(priorities, location) {
  let answer = 1;
  // queue 로 시뮬레이션
  let queue = [];
  // 직접 push
  for (let i = 0; i < priorities.length; i++) {
    queue.push({ index: i, priority: priorities[i] });
  }
  // 찾을때 까지 반복
  while (queue.length > 0) {
    // 현재 큐에서 첫번째 프로세스 빼내기
    const current = queue.shift();
    // 현재 큐 내에서 최대 우선 순위 찾기
    const peek = queue.reduce((acc, curr) => {
      const { priority } = curr;
      return priority > acc ? priority : acc;
    }, -1);
    // 실행 가능
    if (peek <= current.priority) {
      if (current.index === location) {
        return answer;
      } else {
        answer++;
      }
      // 실행 불가능
    } else {
      queue.push(current);
    }
  }
  return -1;
}
