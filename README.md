# roboclaw_rc

This project inlcudes a ROS service by name of roboclaw_node. The name of service is roboclaw_service
That service uses encoder ticks to take a postion of anthing attahced with the motor. 

For the roboclaw project: max ticks=65000 and min ticks=0
  user can put anyvalue in between.
  max ticks and min ticks are not hardcoded or fixed you can also put any value above 65000 and even below 0
  

End Stop:
  An end stop is used with motor on roboclaw pin s4
  The switch s4 is used in non-latch mode( see user manaul for more detail). 
  it work like when motor is moving in one direction and the end stop is pressed. 
  Roboclaw will not take any more command in that direction, it will take command is opposite direction only.
  Like when the motor was moving forward and the end stop button is pressed, The roboclaw will not take forward commands anymore,
  Now it will only take backward commands. till the end stop button is released and the red light is turned off.
