# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Payee'
        db.delete_table(u'transactions_payee')

        # Deleting model 'Payership'
        db.delete_table(u'transactions_payership')

        # Adding model 'Paymentship'
        db.create_table(u'transactions_paymentship', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('transaction', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['transactions.FinancialAgreement'])),
            ('weight_numerator', self.gf('django.db.models.fields.IntegerField')(max_length=100)),
            ('weight_denominator', self.gf('django.db.models.fields.IntegerField')(max_length=100)),
        ))
        db.send_create_signal(u'transactions', ['Paymentship'])

        # Adding model 'FinancialAgreement'
        db.create_table(u'transactions_financialagreement', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('amount', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=10, decimal_places=2)),
            ('party', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['transactions.Party'], null=True, blank=True)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(related_name='agreement_creator', to=orm['auth.User'])),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['transactions.Category'])),
            ('time_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('comments', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('settled', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'transactions', ['FinancialAgreement'])

        # Adding model 'Party'
        db.create_table(u'transactions_party', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=14)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal(u'transactions', ['Party'])

        # Deleting field 'Transaction.category'
        db.delete_column(u'transactions_transaction', 'category_id')

        # Deleting field 'Transaction.has_pair'
        db.delete_column(u'transactions_transaction', 'has_pair')

        # Deleting field 'Transaction.cashflow'
        db.delete_column(u'transactions_transaction', 'cashflow')

        # Deleting field 'Transaction.trans_pair'
        db.delete_column(u'transactions_transaction', 'trans_pair_id')

        # Deleting field 'Transaction.payee'
        db.delete_column(u'transactions_transaction', 'payee_id')

        # Adding field 'Transaction.agreement'
        db.add_column(u'transactions_transaction', 'agreement',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['transactions.FinancialAgreement']),
                      keep_default=False)

        # Adding field 'Transaction.amount'
        db.add_column(u'transactions_transaction', 'amount',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=10, decimal_places=2),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'Payee'
        db.create_table(u'transactions_payee', (
            ('description', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=14)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal(u'transactions', ['Payee'])

        # Adding model 'Payership'
        db.create_table(u'transactions_payership', (
            ('transaction', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['transactions.Transaction'])),
            ('paid_amount', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=10, decimal_places=2)),
            ('payer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('weight_denominator', self.gf('django.db.models.fields.IntegerField')(max_length=100)),
            ('weight_numerator', self.gf('django.db.models.fields.IntegerField')(max_length=100)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'transactions', ['Payership'])

        # Deleting model 'Paymentship'
        db.delete_table(u'transactions_paymentship')

        # Deleting model 'FinancialAgreement'
        db.delete_table(u'transactions_financialagreement')

        # Deleting model 'Party'
        db.delete_table(u'transactions_party')

        # Adding field 'Transaction.category'
        db.add_column(u'transactions_transaction', 'category',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['transactions.Category']),
                      keep_default=False)

        # Adding field 'Transaction.has_pair'
        db.add_column(u'transactions_transaction', 'has_pair',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Transaction.cashflow'
        db.add_column(u'transactions_transaction', 'cashflow',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=10, decimal_places=2),
                      keep_default=False)

        # Adding field 'Transaction.trans_pair'
        db.add_column(u'transactions_transaction', 'trans_pair',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['transactions.Transaction'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Transaction.payee'
        db.add_column(u'transactions_transaction', 'payee',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['transactions.Payee'], null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Transaction.agreement'
        db.delete_column(u'transactions_transaction', 'agreement_id')

        # Deleting field 'Transaction.amount'
        db.delete_column(u'transactions_transaction', 'amount')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'transactions.category': {
            'Meta': {'object_name': 'Category'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        u'transactions.financialagreement': {
            'Meta': {'object_name': 'FinancialAgreement'},
            'amount': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '10', 'decimal_places': '2'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['transactions.Category']"}),
            'comments': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'agreement_creator'", 'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'party': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['transactions.Party']", 'null': 'True', 'blank': 'True'}),
            'settled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'users': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.User']", 'through': u"orm['transactions.Paymentship']", 'symmetrical': 'False'})
        },
        u'transactions.party': {
            'Meta': {'object_name': 'Party'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '14'})
        },
        u'transactions.paymentship': {
            'Meta': {'object_name': 'Paymentship'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'transaction': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['transactions.FinancialAgreement']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'weight_denominator': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'weight_numerator': ('django.db.models.fields.IntegerField', [], {'max_length': '100'})
        },
        u'transactions.transaction': {
            'Meta': {'object_name': 'Transaction'},
            'agreement': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['transactions.FinancialAgreement']"}),
            'amount': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '10', 'decimal_places': '2'}),
            'comments': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'transaction_creator'", 'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Payer'", 'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['transactions']