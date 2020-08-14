# Generated by Django 3.1 on 2020-08-11 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_billitemstest'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillTest2',
            fields=[
                ('purchaseno', models.AutoField(primary_key=True, serialize=False)),
                ('purchase_date', models.DateField(verbose_name='purchase date')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.customerdetail')),
            ],
        ),
        migrations.CreateModel(
            name='BillItemsTest2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productBatch', models.CharField(max_length=50, null=True)),
                ('productPacking', models.CharField(max_length=50, null=True)),
                ('productQuantity', models.IntegerField(default=1)),
                ('productPrice', models.FloatField(default=0)),
                ('productTotalPrice', models.FloatField(default=0)),
                ('productName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bills22', to='shop.productdetailbatch')),
                ('purchaseno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bills22', to='shop.billtest2')),
            ],
        ),
    ]
