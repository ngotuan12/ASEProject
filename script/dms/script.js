db.customer.find({username:"cuongnm"})[0]._id
db.customer.find().forEach(printjson)
db.cus_debit.find({cus_id:db.user.find({username:"cuongnm"})[0]._id}).forEach(printjson)
db.user.find({username:"cuongnm"})[0].forEach(printjson)