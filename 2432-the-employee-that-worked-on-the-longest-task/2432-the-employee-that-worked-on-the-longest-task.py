class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        hard_worker_id = -1
        begin_time = 0
        max_working_time = 0

        for id, leave_time in logs:
            working_time = leave_time - begin_time

            if working_time > max_working_time or (working_time == max_working_time and hard_worker_id > id):
                hard_worker_id = id
                max_working_time = working_time
            begin_time = leave_time
        
        return hard_worker_id