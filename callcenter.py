class Call(object):
    def __init__(self, UID=1, caller="Matt", callerNum="123-4567",callTime=60, callReason="This is a test"):
        self.UID = UID
        self.caller = caller
        self.callerNum = callerNum
        self.callTime = callTime
        self.callReason = callReason
    def display(self):
        print "unique id: {}".format(self.UID)
        print "caller name: {}".format(self.caller)
        print "caller phone number: {}".format(self.callerNum)
        print "time of call: {} min.".format(self.callTime)
        print "reason for call: {}".format(self.callReason)
        return self
    def displayInfo(self):
        print "caller name: {}".format(self.caller)
        print "caller phone number: {}".format(self.callerNum)
        return self

class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.queue_size = len(self.calls)
    def add(self,call):
        if type(call) is Call:
            self.calls.append(call)
            self.queue_size = len(self.calls)
            print "Call added"
        else:
            print "Nothing Added to calls"
        return self
    def remove(self): #removes call at the beginning
        del self.calls[0]
        self.queue_size = len(self.calls)
        return self
    def info(self):
        #Print name and phone for each call
        for call in self.calls:
            print "Call ID: {}".format(call.UID)
            call.displayInfo()
        #Print Length of Queue
        print "Queue Size: {}".format(self.queue_size)
        return self
    #find and remove a call from the queue according to the phone number of the caller
    def removeByPhone(self,phone):
        if type(phone) is str:
            for i in range(0,len(self.calls)):
                if self.calls[i].callerNum == phone:
                    del self.calls[i]
                    self.queue_size = len(self.calls)
center = CallCenter()
c1 = Call()
c2 = Call(2,"Tiffany","555-1111",20,"Second Call")
c3 = Call(2,"Bob","666-1111",20,"Third Call")
center.add(Call()).add(c2).add(c3).add("Harry").remove()
center.info()
center.removeByPhone("666-1111")
center.info()