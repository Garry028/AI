n = 3  # number of jobs
#  job-id , time , profit
# TC->O(n)
# SC->O(n)
jobs = [['Job1', '2', '100'], ['Job2', '3', '450'], ['Job3', '3', '325']]
# extract profit from jobs
sorter = lambda job: int(job[2])
# this will sort based on profit in descending order
jobs = sorted(jobs, key=sorter, reverse=True)
# empty array for storing scheduled jobs
scheduled = []
# time is zero initially
time = 0
# This condition checks if the current time is less than or equal to the job's deadline (accessed using i[1]). If the condition is true, the job can be scheduled.
for i in jobs:
    deadline =int(i[1])
    jobId=i[0]
    if time <=deadline :
        scheduled.append(jobId)
        time += 1

print("Jobs are scheduled as:")
print(scheduled)
