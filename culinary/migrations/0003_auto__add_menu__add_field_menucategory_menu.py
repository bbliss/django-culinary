# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Menu'
        db.create_table('culinary_menu', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('culinary', ['Menu'])

        # Adding field 'MenuCategory.menu'
        db.add_column('culinary_menucategory', 'menu', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['culinary.Menu']), keep_default=False)


    def backwards(self, orm):
        
        # Deleting model 'Menu'
        db.delete_table('culinary_menu')

        # Deleting field 'MenuCategory.menu'
        db.delete_column('culinary_menucategory', 'menu_id')


    models = {
        'culinary.menu': {
            'Meta': {'object_name': 'Menu'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'culinary.menucategory': {
            'Meta': {'object_name': 'MenuCategory'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'menu': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['culinary.Menu']"}),
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
            'after_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'after_time': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'auto': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'menu_item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['culinary.MenuItem']"}),
            'until_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'until_time': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'weekday': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'})
        }
    }

    complete_apps = ['culinary']
