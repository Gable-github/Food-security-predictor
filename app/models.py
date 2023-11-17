from app import db

class Dataset_climate(db.Model):
	__tablename__ = 'data_climate'
	id = db.Column(db.Integer, primary_key=True)
	price_var = db.Column(db.Float)
	indep_var = db.Column(db.String(50))

	def __repr__(self):
		return f"<PriceData - Price: {self.price}, Weather Pattern: {self.weather_pattern}>"
	
# # use this only if need to make a main table, else routes can reference each table separately
# class Dataset(db.Model):
# 	__tablename__ = 'dataset'
# 	id = db.Column(db.Integer, primary_key=True)
# 	dataset = db.Column(db.String(50))

# 	data_climate = db.relationship("Data_climate", back_populates="Dataset")



#db.create_all()