# -*- coding: utf-8 -*-
# Copyright 2013, Benjamin Coudrin, LIRMM, CNRS
# Copyright 2011, Florent Lamiraux, Thomas Moulard, JRL, CNRS/AIST
#
# This file is part of dynamic-graph.
# dynamic-graph is free software: you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation, either version 3 of
# the License, or (at your option) any later version.
#
# dynamic-graph is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Lesser Public License for more details.  You should have
# received a copy of the GNU Lesser General Public License along with
# dynamic-graph. If not, see <http://www.gnu.org/licenses/>.

#from dynamic_graph.sot.dynamics.abstract_robot import AbstractRobot
from dynamic_graph.sot.dynamics.mobile_robot_v3 import AbstractMobileRobot
from dynamic_graph.ros import RosRobotModel
from dynamic_graph.sot.core import  SOT,FeaturePosition, Task
from rospkg import RosPack
import pinocchio as se3

class Ur5(AbstractMobileRobot):
    """
    This class instanciates a Ur5 robot.
    """

    tracedSignals = {
        'dynamic': ["com", "position", "velocity", "acceleration"],
        'device': ['control', 'state']
        }
        
    #initPosition = [0,0,0,0,0,0,0.011,0.011,-0.1, 0.023, 0.12,0,0]
    
    def __init__(self, name, device = None, tracer = None):
        AbstractMobileRobot.__init__ (self, name, tracer)
        # add operational points
        self.OperationalPoints.append('root_joint')
        self.OperationalPoints.append('shoulder_pan_joint')
        self.OperationalPoints.append('shoulder_lift_joint')
        self.OperationalPoints.append('elbow_joint')
        self.OperationalPoints.append('wrist_1_joint')
        self.OperationalPoints.append('wrist_2_joint')
        self.OperationalPoints.append('wrist_3_joint')
        self.OperationalPoints.append('forerarm_skin_root_cell_joint')
        self.OperationalPoints.append('forerarm_skin_cell_joint_0')
        self.OperationalPoints.append('forerarm_skin_cell_joint_1')
        self.OperationalPoints.append('forerarm_skin_cell_joint_2')
        self.OperationalPoints.append('forerarm_skin_cell_joint_3')
        self.OperationalPoints.append('forerarm_skin_cell_joint_4')
        self.OperationalPoints.append('forerarm_skin_cell_joint_5')
        self.OperationalPoints.append('forerarm_skin_cell_joint_6')
        self.OperationalPoints.append('forerarm_skin_cell_joint_7')        

        # device and dynamic model assignment
        self.device = device
        rospack = RosPack()
	self.urdfDir = rospack.get_path('sot_robot') + '/urdf/'
        print "Loaded model...."
        self.urdfName = 'ur5_robot_with_ring_forearm.urdf'
        self.pinocchioModel = se3.buildModelFromUrdf(self.urdfDir + self.urdfName,
                                                     se3.JointModelFreeFlyer())
        self.pinocchioData = self.pinocchioModel.createData()

        self.dynamic = RosRobotModel("{0}_dynamic".format(name))
        self.dynamic.setModel(self.pinocchioModel)
        self.dynamic.setData(self.pinocchioData)

        # load model
        #self.dynamic.loadFromParameterServer()
        self.dimension = self.dynamic.getDimension()
        #self.initPosition = ip
        self.initPosition = (-1.,) * self.dimension
        # initialize ur robot
        self.initializeRobot()        
__all__ = ["Ur5"]

