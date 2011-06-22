# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'MenuCategory'
        db.create_table('culinary_menucategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=100, db_index=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('culinary', ['MenuCategory'])

        # Adding model 'MenuItem'
        db.create_table('culinary_menuitem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['culinary.MenuCategory'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('spicyness', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('goes_well_with', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['culinary.MenuItem'], null=True, blank=True)),
            ('healthy_choice', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('gluten_free', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('low_carb', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('vegan', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('price', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('price_with_combo', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
        ))
        db.send_create_signal('culinary', ['MenuItem'])

        # Adding model 'Special'
        db.create_table('culinary_special', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('menu_item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['culinary.MenuItem'])),
            ('auto', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('weekday', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('after_time', self.gf('django.db.models.fields.TimeField')(blank=True)),
            ('until_time', self.gf('django.db.models.fields.TimeField')(blank=True)),
            ('after_date', self.gf('django.db.models.fields.DateField')(blank=True)),
            ('until_date', self.gf('django.db.models.fields.DateField')(blank=True)),
        ))
        db.send_create_signal('culinary', ['Special'])


    def backwards(self, orm):
        
        # Deleting model 'MenuCategory'
        db.delete_table('culinary_menucategory')

        # Deleting model 'MenuItem'
        db.delete_table('culinary_menuitem')

        # Deleting model 'Special'
        db.delete_table('culinary_special')


    models = {
        'culinary.menucategory': {
            'Meta': {'object_name': 'MenuCategory'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'culinary.menuitem': {
            'Meta': {'object_name': 'MenuItem'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['culinary.MenuCategory']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'gluten_free': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'goes_well_with': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['culinary.MenuItem']", 'null': 'True', 'blank': 'True'}),
            'healthy_choice': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'low_carb': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'price': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'price_with_combo': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'spicyness': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'vegan': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'culinary.special': {
            'Meta': {'object_name': 'Special'},
            'after_date': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'after_time': ('django.db.models.fields.TimeField', [], {'blank': 'True'}),
            'auto': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'menu_item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['culinary.MenuItem']"}),
            'until_date': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'until_time': ('django.db.models.fields.TimeField', [], {'blank': 'True'}),
            'weekday': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'})
        }
    }

    complete_apps = ['culinary']
