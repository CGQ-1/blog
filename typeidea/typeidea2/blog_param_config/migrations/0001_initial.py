# Generated by Django 3.2.14 on 2022-07-17 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog_config',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', models.CharField(blank=True, help_text='数字类型编码, 相同的编码表示为统一类型', max_length=12, null=True, verbose_name='参数类型')),
                ('TypeDesc', models.CharField(blank=True, help_text='一般为英文解释, 表示这一类型的属性', max_length=32, null=True, verbose_name='参数类型描述')),
                ('TypeName', models.CharField(blank=True, help_text='一般为中文描述, 表示这一类型的用途', max_length=32, null=True, verbose_name='参数类型名称')),
                ('Seq', models.IntegerField(blank=True, help_text='无实际意义,一般用来排序', null=True, verbose_name='参数序号')),
                ('V', models.CharField(blank=True, help_text='填写你需要的值,比如类型,姓名等', max_length=255, null=True, verbose_name='参数值')),
                ('VDesc', models.TextField(blank=True, help_text='填写对你需要值的补充，可以和参数值相同，也可以不同', null=True, verbose_name='参数值描述')),
                ('UpdateTime', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '系统参数配置',
                'verbose_name_plural': '系统参数配置',
                'ordering': ['Type', 'Seq'],
            },
        ),
    ]
