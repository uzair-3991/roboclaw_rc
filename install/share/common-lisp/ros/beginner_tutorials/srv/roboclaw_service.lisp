; Auto-generated. Do not edit!


(cl:in-package beginner_tutorials-srv)


;//! \htmlinclude roboclaw_service-request.msg.html

(cl:defclass <roboclaw_service-request> (roslisp-msg-protocol:ros-message)
  ((enc
    :reader enc
    :initarg :enc
    :type cl:integer
    :initform 0))
)

(cl:defclass roboclaw_service-request (<roboclaw_service-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <roboclaw_service-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'roboclaw_service-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name beginner_tutorials-srv:<roboclaw_service-request> is deprecated: use beginner_tutorials-srv:roboclaw_service-request instead.")))

(cl:ensure-generic-function 'enc-val :lambda-list '(m))
(cl:defmethod enc-val ((m <roboclaw_service-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader beginner_tutorials-srv:enc-val is deprecated.  Use beginner_tutorials-srv:enc instead.")
  (enc m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <roboclaw_service-request>) ostream)
  "Serializes a message object of type '<roboclaw_service-request>"
  (cl:let* ((signed (cl:slot-value msg 'enc)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 18446744073709551616) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <roboclaw_service-request>) istream)
  "Deserializes a message object of type '<roboclaw_service-request>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'enc) (cl:if (cl:< unsigned 9223372036854775808) unsigned (cl:- unsigned 18446744073709551616))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<roboclaw_service-request>)))
  "Returns string type for a service object of type '<roboclaw_service-request>"
  "beginner_tutorials/roboclaw_serviceRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'roboclaw_service-request)))
  "Returns string type for a service object of type 'roboclaw_service-request"
  "beginner_tutorials/roboclaw_serviceRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<roboclaw_service-request>)))
  "Returns md5sum for a message object of type '<roboclaw_service-request>"
  "9e36e203987fc6183576e3695ee8044e")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'roboclaw_service-request)))
  "Returns md5sum for a message object of type 'roboclaw_service-request"
  "9e36e203987fc6183576e3695ee8044e")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<roboclaw_service-request>)))
  "Returns full string definition for message of type '<roboclaw_service-request>"
  (cl:format cl:nil "int64 enc~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'roboclaw_service-request)))
  "Returns full string definition for message of type 'roboclaw_service-request"
  (cl:format cl:nil "int64 enc~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <roboclaw_service-request>))
  (cl:+ 0
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <roboclaw_service-request>))
  "Converts a ROS message object to a list"
  (cl:list 'roboclaw_service-request
    (cl:cons ':enc (enc msg))
))
;//! \htmlinclude roboclaw_service-response.msg.html

(cl:defclass <roboclaw_service-response> (roslisp-msg-protocol:ros-message)
  ((return_enc
    :reader return_enc
    :initarg :return_enc
    :type cl:integer
    :initform 0))
)

(cl:defclass roboclaw_service-response (<roboclaw_service-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <roboclaw_service-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'roboclaw_service-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name beginner_tutorials-srv:<roboclaw_service-response> is deprecated: use beginner_tutorials-srv:roboclaw_service-response instead.")))

(cl:ensure-generic-function 'return_enc-val :lambda-list '(m))
(cl:defmethod return_enc-val ((m <roboclaw_service-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader beginner_tutorials-srv:return_enc-val is deprecated.  Use beginner_tutorials-srv:return_enc instead.")
  (return_enc m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <roboclaw_service-response>) ostream)
  "Serializes a message object of type '<roboclaw_service-response>"
  (cl:let* ((signed (cl:slot-value msg 'return_enc)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 18446744073709551616) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <roboclaw_service-response>) istream)
  "Deserializes a message object of type '<roboclaw_service-response>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'return_enc) (cl:if (cl:< unsigned 9223372036854775808) unsigned (cl:- unsigned 18446744073709551616))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<roboclaw_service-response>)))
  "Returns string type for a service object of type '<roboclaw_service-response>"
  "beginner_tutorials/roboclaw_serviceResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'roboclaw_service-response)))
  "Returns string type for a service object of type 'roboclaw_service-response"
  "beginner_tutorials/roboclaw_serviceResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<roboclaw_service-response>)))
  "Returns md5sum for a message object of type '<roboclaw_service-response>"
  "9e36e203987fc6183576e3695ee8044e")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'roboclaw_service-response)))
  "Returns md5sum for a message object of type 'roboclaw_service-response"
  "9e36e203987fc6183576e3695ee8044e")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<roboclaw_service-response>)))
  "Returns full string definition for message of type '<roboclaw_service-response>"
  (cl:format cl:nil "int64 return_enc~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'roboclaw_service-response)))
  "Returns full string definition for message of type 'roboclaw_service-response"
  (cl:format cl:nil "int64 return_enc~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <roboclaw_service-response>))
  (cl:+ 0
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <roboclaw_service-response>))
  "Converts a ROS message object to a list"
  (cl:list 'roboclaw_service-response
    (cl:cons ':return_enc (return_enc msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'roboclaw_service)))
  'roboclaw_service-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'roboclaw_service)))
  'roboclaw_service-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'roboclaw_service)))
  "Returns string type for a service object of type '<roboclaw_service>"
  "beginner_tutorials/roboclaw_service")