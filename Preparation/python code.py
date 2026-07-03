### Given a list of integers and a target number, return the indices of the two numbers that add up to the target. ####
nums = [2, 7, 11, 15]
target = 9

seen={}
for i,j in enumerate(nums):
    find=target-j
    if find in seen:
        print(seen[find],i)
    seen[j]=i

### Longest Substring Without Repeating Characters ###
 
s='aabbd'
seen=set()
left=0
max_len=0
for right in range(len(s)):
    while s[right] in seen:
        seen.remove(s[left])
        left+=1
    seen.add(s[right])
    max_len = max(max_len, right-left+1)
print(max_len)


### Anagram Check ###
s1 = "listen"  
s2 = "silent"

## using sort ##
if sorted(s1) == sorted(s2):
    print(True)
else:
    print(False)

## w/o sort ##
char_freq={}
for i in s1:
    char_freq[i]=char_freq.get(i, 0)+1

for j in s2:
    if j not in char_freq:
        print(False)
    char_freq[j]-=1
    if char_freq[j]<0:
        print(False)
print(True)


#### Flatten a Nested List ####

f_list=[1, [2, 3], [4, [5, 6]], 7]

def flattern_list(f_list):
    users=[]
    for i in f_list:
        if isinstance(i, list):
            users.extend(flattern_list(i))
        else:
            users.append(i)
    return users
print(flattern_list(f_list))


### Find Duplicates in a List ###
user_list = [1, 2, 3, 2, 4, 3, 5]
count_freq={}
for i in user_list:
    count_freq[i]=count_freq.get(i, 0)+1

new_list=[]
for j in set(user_list):
    if count_freq[j]>1:
        new_list.append(j)

print(new_list)


### Valid Parentheses ###

s = "()"

start=[]
par_dict={'}':'{',']':'[',')':'('}
for i in s:
    if i in ['}',')',']']:
        if start[-1] != par_dict[i]:
            print(False)
        else:
            start.pop()
    else:
        start.append(i)
print(True,start)


### Second Largest Number ###

s=[1, 2, 3, 4, 5, 5]
first=float('-inf')
second = float('-inf')

for i in s:
    if first < i:
        second = first
        first = i
    elif second < i and i != first:
        second = i
print(second)

### Anagram ###

s=["eat", "tea", "tan", "ate", "nat", "bat"]

simliar_dict={}
for i in s:
    sorted_text = ''.join(sorted(i))
    if sorted_text in simliar_dict.keys():
        simliar_dict[sorted_text].append(i)
    else:
        simliar_dict[sorted_text]=[i]
ana_group = [i for i in simliar_dict.values()]
print(ana_group)

### Binary Search ###

nums = [1, 3, 5, 7, 9, 11]
target = 7

def binary_search(nums,target):
    i=0
    j=len(nums)-1

    while i <= j:
        mid=(i+j)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            i = mid+1
        else:
            j = mid-1
    return -1
print(binary_search(nums,target))


### Climbing Stairs ###
n=5
if n<=2:
    print(n)

prev2 = 1
prev1 = 2
for i in range(3,n+1):
    curr = prev2+prev1
    prev2 = prev1
    prev1 = curr

print(prev1)


###  Maximum Subarray Sum (Kadane's Algorithm) ###

nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]

max_val=0
max_sum = 0
for i in nums:
    max_val=max(max_val+i,i)
    max_sum = max(max_val,max_sum)

print(max_sum)


### Count Occurrences of Each Character ###
from collections import Counter
word = "hello world"

word_freq = Counter(word)
print(dict(word_freq.most_common()))
print(dict(sorted(dict(word_freq).items(), key=lambda x:x[1], reverse=True)))


###  Reverse a Linked List ###

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

    def reverse(self):
        curr = self.head
        prev = None

        while curr is not None:
            next_node = curr.next
            curr.next=prev
            prev = curr
            curr = next_node

        self.head = prev

### Find Missing Numbers ###

nums=[1, 2, 4, 5, 6]  
n=6

# method one
for i in range(1,n+1):
    if i not in nums:
        print(i)

# method two
expe_sum = sum(list(range(1,6+1))) # or n * (n+1) //2
actual_sum =sum(nums)

missing = expe_sum-actual_sum
print(missing)


### : Palindrome Check ###

# words = "racecar"
words = "hello"

i=0
j=len(words)-1

while i <=j:
    if words[i] != words[j]:
        print(False)
        break
    i+=1
    j-=1

print(True)

### Two Sum II (Sorted Array) Using Two Pointer ###

nums = [2, 7, 11, 15]
target = 9

nums = [-1, 0]
target = -1

i=0
j=len(nums)-1

while i<=j:
    if nums[i]+nums[j] == target:
        print(i,j)
        break
    elif nums[i]+nums[j] > target:
        j-=1
    else:
        i+=1
       
### Two Sum II  Using windows  ###

nums=[3,7,2,5,6,8,9]
target = 9
left = 0
curr_sum=0

for right in range(len(nums)):
    curr_sum+=nums[right]
    while curr_sum > target and left <=right:
        curr_sum-=nums[left]
        left+= 1

    if target == curr_sum:
        print(nums[left:right+1],'windows two sum')

### Product of Array Except Self ###
import math

nums =[1, 2, 3, 4]
prods = []
print(list(range(len(nums)-2, -1, -1)),'sdssssss')
print([1] * len(nums))
for i in range(len(nums)):
    pre = nums[:i]
    suf = nums[i+1:]
    prev_pro = math.prod(pre)
    suff_pro = math.prod(suf)
    prods.append(prev_pro * suff_pro )

print(prods)
   

### generator

nums =[1, 2, 3, 4]
def gen(nums):
    for i in nums:
        yield i
gen_obj = gen(nums)
print(gen_obj.__next__())
print(gen_obj.__next__())
print(gen_obj.__next__())
print(gen_obj.__next__())

## iteration
iteration = iter(nums)
print(next(iteration),'sdf')
print(next(iteration),'sdf')
print(next(iteration),'sdf')


### fibbnosis ###

def fib(n):
    a,b = 0,1
    for i in range(n):
        print(a,end=' ')
        a,b = b,a+b
print(fib(10))

### Prime number
num=20
prime=True
for i in range(2,int(num**0.5)+1):
    if num%2 == 0:
        prime=False
        break

print(prime)

### Factorial ###
def Factorial(n):
    if n==1 or n==2:
        return n
    return n*Factorial((n-1))



### mergge inteval

def merge(intervals):
    intervals.sort()
    res = [intervals[0]]
    print(res)
    for s, e in intervals[1:]:
        last_e = res[-1]
        if s <= last_e:
            res[-1][1] = max(last_e, e)
        else:
            res.append([s, e])
    return res
print(merge([[1,3],[2,6],[8,10],[15,18]]))


### LRU ###
from collections import OrderedDict
class LRUCache:
    def __init__(self, cap):
        self.cap = cap
        self.cache = OrderedDict()
    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]
    def put(self, key, val):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = val
        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)


### Cycle in Linked List ###
def cycle(head):
    slow=fast=head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

### max subsum k len ###
arr=[2,1,5,1,3,2]
k=3

def sub_sum(arr,k):
    wind_sum=sum(arr[:k])
    max_val=wind_sum

    for i in range(k,len(arr)):
        wind_sum += arr[i] - arr[i-k]
        max_val = max(max_val,wind_sum)

    return max_val
print(sub_sum(arr,k))


def flatten(d, parent=""):
    res = {}
    for k, v in d.items():
        new_key = f"{parent}.{k}" if parent else k
        if isinstance(v, dict):
            res.update(flatten(v, new_key))
        else:
            res[new_key] = v
    return res
print(flatten({"a":{"b":1,"c":{"d":2}}}))


inputs ='abcdef'

seen=set()
i=0
max_len=0
con_chart=0
for j in range(len(inputs)):
    while inputs[j] in seen:
        seen.remove(inputs[i])
        i+=1
    seen.add(inputs[j])
   
    if j-i+1 > max_len:
        max_len =j-i+1
        con_chart=1
input[con_chart:con_chart+max_len]

print(max_len)
   
   
alerts = [
    {"id": 1, "severity": "high", "status": "open",   "timestamp": "2024-01-03"},
    {"id": 2, "severity": "low",  "status": "open",   "timestamp": "2024-01-01"},
    {"id": 3, "severity": "high", "status": "closed", "timestamp": "2024-01-02"},
    {"id": 4, "severity": "high", "status": "open",   "timestamp": "2024-01-01"},
    {"id": 5, "severity": "medium","status": "open",  "timestamp": "2024-01-02"},
]


high_open_alerts=[]

for i in alerts:
    if i["severity"]== "high" and  i["status"]=="open":
        high_open_alerts.append(i)
   
print(sorted(high_open_alerts, key= lambda x : x['timestamp']))


data={
    "status": "success",
    "data": {
        "alerts": [
            {"id": "A1", "type": "malware",   "risk": 9},
            {"id": "A2", "type": "phishing",  "risk": 4},
            {"id": "A3", "type": "bruteforce","risk": 7},
            {"id": "A4", "type": "malware",   "risk": 6},
        ]
    }
}

def get_high_risk_alerts(response):
    high_alert = []
    if response['status'] == 'success':
        data = response['data']['alerts']
        for alert in data:
            if alert['risk'] >= 7:
                high_alert.append(alert)
    else:
        high_alert = []
       
    if high_alert:
        return sorted(high_alert, key=lambda x: -x['risk'])
       
    return high_alert
   
print(get_high_risk_alerts(data))


# Design a base class SecurityConnector with:
# - __init__(self, platform_name, api_key)
# - connect(self)        → prints "Connecting to {platform_name}..."
# - fetch_alerts(self)   → raises NotImplementedError (must be overridden)
# - status(self)         → returns "Connected" or "Disconnected"
#                          (track this with a self.connected bool)
#
# Then create a subclass SplunkConnector that:
# - Calls parent __init__
# - Overrides fetch_alerts() to return:
#   [{"id": "S1", "source": "Splunk", "risk": 8}]
# - Overrides connect() to set self.connected = True
#   AND still prints the parent's connect message
#
# Expected behaviour:
# sc = SplunkConnector("Splunk", "abc123")
# print(sc.status())       → "Disconnected"
# sc.connect()             → "Connecting to Splunk..."
# print(sc.status())       → "Connected"
# print(sc.fetch_alerts()) → [{"id": "S1", "source": "Splunk", "risk": 8}]

class SecurityConnector:
    def __init__(self,platform_name, api_key):
        self.platform_name = platform_name
        self.api_key = api_key
    def connect(self):
        print(f'Connecting to {self.platform_name}...')
   
    def fetch_alerts(self):
        return [{"id": "S1", "source": f"self.platform_name", "risk": 8}]
       
    def status(self):
        if self.platform_name:
            return 'Connected'
        else:
            return 'Disconnected'

class SplunkConnector(SecurityConnector):
    def __init__(self,platform_name, api_key):
        super().__init__(platform_name, api_key)
       
       
logs = [
    "2024-01-01 08:00:00,192.168.1.1,10.0.0.1,443,ALLOW",
    "2024-01-01 08:01:00,192.168.1.2,10.0.0.2,22,BLOCK",
    "2024-01-01 08:02:00,192.168.1.1,10.0.0.3,80,BLOCK",
    "2024-01-01 08:03:00,192.168.1.3,10.0.0.1,443,BLOCK",
    "2024-01-01 08:04:00,192.168.1.2,10.0.0.2,22,BLOCK",
    "2024-01-01 08:05:00,192.168.1.1,10.0.0.3,8080,BLOCK",
    "2024-01-01 08:06:00,192.168.1.4,10.0.0.4,443,ALLOW",
    "2024-01-01 08:07:00,192.168.1.3,10.0.0.1,22,BLOCK",
    "2024-01-01 08:08:00,192.168.1.2,10.0.0.2,80,BLOCK",
    "2024-01-01 08:09:00,192.168.1.1,10.0.0.3,22,ALLOW",
]


def analyze_logs(logs):
   
    top_blocked_ips={}
    port=set()
    block_count = 0
    for log in logs:
        log_arr=log.split(',')
        if log_arr[4] == 'BLOCK':
            top_blocked_ips[log_arr[1]]=top_blocked_ips.get(log_arr[1],0)+1
            port.add(log_arr[3])
            block_count+=1
   
    per_block = (block_count/len(logs))*100
    top_blocked_ips = sorted(top_blocked_ips.items(), key = lambda x : (-x[1],x[0]))
   
    return {'top_blocked_ips':top_blocked_ips,'unique_ports':port,'block_rate':per_block}
   
   
alerts = [
    {"id": 1, "source_ip": "192.168.1.1", "event_type": "malware",    "risk": 9},
    {"id": 2, "source_ip": "192.168.1.2", "event_type": "phishing",   "risk": 4},
    {"id": 3, "source_ip": "192.168.1.1", "event_type": "malware",    "risk": 6},  # dup of id 1
    {"id": 4, "source_ip": "192.168.1.3", "event_type": "bruteforce", "risk": 7},
    {"id": 5, "source_ip": "192.168.1.2", "event_type": "phishing",   "risk": 4},  # dup of id 2
    {"id": 6, "source_ip": "192.168.1.3", "event_type": "bruteforce", "risk": 7},  # dup of id 4
    {"id": 7, "source_ip": "192.168.1.4", "event_type": "ransomware", "risk": 3},
]

def process_alerts(alerts):
    sorted_alert=[]
    for alert in alerts:
        ip = alert['source_ip']
        dup=False
        for sort_al in sorted_alert:
            if ip == sort_al["source_ip"] and alert['risk'] > sort_al['risk']:
                sorted_alert.remove(sort_al)
                if alert['risk'] >= 8:
                    alert['priority'] = 'critical'
                elif alert['risk'] >=5:
                    alert['priority'] = 'medium'
                else:
                    alert['priority'] = 'low'
                sorted_alert.append(alert)
                dup = True
            elif ip == sort_al["source_ip"] :
                dup = True
        if not dup:
            if alert['risk'] >= 8:
                alert['priority'] = 'critical'
            elif alert['risk'] >=5:
                alert['priority'] = 'medium'
            else:
                alert['priority'] = 'low'
            sorted_alert.append(alert)
   
    sorted_alert = sorted(sorted_alert, key= lambda x: -x['risk'])
    return sorted_alert

print(process_alerts(alerts))
   
json={
    "status": "success",
    "data": {
        "alerts": [
            {"id": 1, "source_ip": "10.0.0.1", "event_type": "malware",    "risk": 9},
            {"id": 2, "source_ip": "10.0.0.2", "event_type": "phishing",   "risk": 4},
            {"id": 3, "source_ip": "10.0.0.3", "event_type": "bruteforce", "risk": 7},
            {"id": 4, "source_ip": "10.0.0.1", "event_type": "ransomware", "risk": 5},
        ]
    }
}

print(json.get('data',{}).get('alerts',[]))









































