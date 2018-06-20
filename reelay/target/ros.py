class RosNodeGenerator:

    def __init__(self, name, roscfg):

        super().__init__()
        self.statements = []

        self.name = name
        self.topic_input = roscfg['topic_input']
        self.topic_output = roscfg['topic_output']
        self.assign = roscfg['assign']
        self.message_type = roscfg['message_type']
        self.include = ["ros/ros.h", "std_msgs/Bool.h"] + roscfg['include']

    def generate(self, states=None, meta=None):

        for library in self.include:
            self.statements.append('#include "{}"'.format(library))

        self.statements.append('')
        self.statements.append('#include "Monitor{}.hpp"'.format(self.name))

        self.statements.append('')
        self.statements.append('struct Monitor{name}Handler : Monitor{name}'.format(name=self.name) + ' {')
        self.statements.append('')
        self.statements.append('\tros::NodeHandle nh;')
        self.statements.append('')
        self.statements.append('\tros::Subscriber sub = nh.subscribe("{topic_name}", 1, &Monitor{name}Handler::callback, this);'.format(topic_name=self.topic_input, name=self.name))
        self.statements.append('\tros::Publisher pub = nh.advertise<std_msgs::Bool>("{topic_name}", 1);'.format(topic_name=self.topic_output))
        self.statements.append('\tstd_msgs::Bool msgout;')
        self.statements.append('')
        self.statements.append('\tvoid callback(const {msgtype} &msg)'.format(msgtype=self.message_type) + '{') 
        self.statements.append('')
        self.statements.append('\t\tthis->update({args});'.format(args=', '.join(['msg.'+self.assign[var[1]] for var in sorted(meta['vars'])])))
        self.statements.append('\t\tmsgout.data = this->output();')
        self.statements.append('\t\tpub.publish(msgout);')
        self.statements.append('\t}')
        self.statements.append('};')
        self.statements.append('')
        self.statements.append('int main(int argc, char **argv){')
        self.statements.append('')
        self.statements.append('\tros::init(argc, argv, "{name}");'.format(name=self.name))
        self.statements.append('\tMonitor{name}Handler mh = Monitor{name}Handler();'.format(name=self.name))
        self.statements.append('\tros::spin();')
        self.statements.append('\treturn 0;')
        self.statements.append('}')

        code = '\n'.join(self.statements)

        return code