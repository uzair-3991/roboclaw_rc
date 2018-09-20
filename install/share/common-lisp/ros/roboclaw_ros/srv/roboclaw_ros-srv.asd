
(cl:in-package :asdf)

(defsystem "roboclaw_ros-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "roboclaw_service" :depends-on ("_package_roboclaw_service"))
    (:file "_package_roboclaw_service" :depends-on ("_package"))
  ))