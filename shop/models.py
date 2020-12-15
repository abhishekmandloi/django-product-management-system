from django.db import models
# Create your models here.

class Ingredient(models.Model):
    ingredient = models.CharField(max_length=300)

    def __str__(self):
        return self.ingredient

class HSNCode(models.Model):
    hsn_code = models.CharField(max_length=50)
    rate = models.FloatField(default=18.0)

    def __str__(self):
        return "{}_ ({} %)".format(self.hsn_code,self.rate)

class Product(models.Model):
    company = models.CharField(max_length=100, default='None')
    product = models.CharField(max_length=100)
    # ingredients = models.CharField(max_length=300)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='ingredients',default='None')
    hsn_code = models.ForeignKey(HSNCode, on_delete=models.CASCADE, related_name='ingredients',default='None')

    def __str__(self):
        return self.product

class ProductDetail(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    batch_no = models.CharField(max_length=50)
    mfgdate = models.DateTimeField('manufacture')
    expirydate = models.DateTimeField('expiry date')
    packing = models.CharField(max_length=50)
    quantity = models.IntegerField(default=0)
    price = models.FloatField(default=0)

    def __str__(self):
        return "{}_{}_{}".format(self.product.product, self.batch_no, self.packing)

class ProductBatch(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    batch_no = models.CharField(max_length=50, default='')
    mfgdate = models.DateField('manufacture')
    expirydate = models.DateField('expiry date')
    # packing = models.CharField(max_length=50)
    # quantity = models.IntegerField(default=0)
    # price = models.FloatField(default=0)

    def __str__(self):
        return "{}_{}".format(self.product.product, self.batch_no)

class ProductDetailBatch(models.Model):
    # product = models.ForeignKey(Product, on_delete=models.CASCADE)
    batch_no = models.ForeignKey(ProductBatch, on_delete=models.CASCADE) #models.CharField(max_length=50)
    packing = models.CharField(max_length=50, default='')
    quantity = models.IntegerField(default=0)
    price = models.FloatField(default=0)

    def __str__(self):
        return "{}_{}_{}".format(self.batch_no.product.product,self.batch_no.batch_no, self.packing)

class CustomerDetail(models.Model):
    name = models.CharField(max_length=100)
    joining_date = models.DateField('joining date', auto_now_add=True)
    address = models.CharField(max_length=150,blank=True)
    mobile_no = models.BigIntegerField(blank=True,null=True)

    def __str__(self):
        if self.mobile_no:
            return "{} {}".format(self.name, self.mobile_no)
        else:
            return "{}".format(self.name)

class Bill(models.Model):
    purchaseno = models.IntegerField(default=1)
    customer = models.ForeignKey(CustomerDetail, on_delete=models.CASCADE)
    purchase_date = models.DateField('purchase date')

    def __str__(self):
        return "{}_{}".format(self.customer.name,self.purchaseno)

class BillItems(models.Model):
    purchaseno = models.ForeignKey(Bill, related_name="bills", on_delete=models.CASCADE)
    # productName = self.product.batch_no.product.product
    # productBatch = self.product.batch_no.batch_no
    # productPacking = self.product.packing
    # productQuantity = models.IntegerField()
    # productPrice = self.product.price
    # productTotalPrice = self.productQuantity * self.productPrice
    productName = models.CharField(max_length=100,null=True)
    productBatch = models.CharField(max_length=50,null=True)
    productPacking = models.CharField(max_length=50,null=True)
    productQuantity = models.IntegerField(default=1)
    productPrice = models.FloatField(default=0)
    productTotalPrice = models.FloatField(default=0) #self.productQuantity * self.productPrice

    def __str__(self):
        return "{}".format(self.purchaseno.purchaseno)
    
    def getProductName(self):
        return "Product Name: {}".format(self.bills.purchaseno)

class BillItemsTest(models.Model):
    purchaseno = models.ForeignKey(Bill, related_name="bills2", on_delete=models.CASCADE)
    # productName = self.product.batch_no.product.product
    # productBatch = self.product.batch_no.batch_no
    # productPacking = self.product.packing
    # productQuantity = models.IntegerField()
    # productPrice = self.product.price
    # productTotalPrice = self.productQuantity * self.productPrice
    productName = models.ForeignKey(ProductDetailBatch, related_name="bills2", on_delete=models.CASCADE)
    productBatch = models.CharField(max_length=50,null=True)
    productPacking = models.CharField(max_length=50,null=True)
    productQuantity = models.IntegerField(default=1)
    productPrice = models.FloatField(default=0)
    productTotalPrice = models.FloatField(default=0) #self.productQuantity * self.productPrice

    def __str__(self):
        return "{}".format(self.purchaseno.purchaseno)
    
    def getProductName(self):
        return "Product Name: {}".format(self.bills.purchaseno)


class BillTest2(models.Model):
    purchaseno = models.AutoField(primary_key=True)
    customer = models.ForeignKey(CustomerDetail, on_delete=models.CASCADE)
    purchase_date = models.DateField('purchase date')

    def __str__(self):
        return "{}_{}".format(self.customer.name,self.purchaseno)

class BillItemsTest2(models.Model):
    purchaseno = models.ForeignKey(BillTest2, related_name="bills22", on_delete=models.CASCADE)
    # productName = self.product.batch_no.product.product
    # productBatch = self.product.batch_no.batch_no
    # productPacking = self.product.packing
    # productQuantity = models.IntegerField()
    # productPrice = self.product.price
    # productTotalPrice = self.productQuantity * self.productPrice
    productName = models.ForeignKey(ProductDetailBatch, related_name="bills22", on_delete=models.CASCADE)
    productBatch = models.CharField(max_length=50,null=True)
    productPacking = models.CharField(max_length=50,null=True)
    productQuantity = models.IntegerField(default=1)
    productPrice = models.FloatField(default=0)
    productTotalPrice = models.FloatField(default=0) #self.productQuantity * self.productPrice

    def __str__(self):
        return "{}".format(self.purchaseno.purchaseno)
    
    def getProductName(self):
        return "Product Name: {}".format(self.bills.purchaseno)