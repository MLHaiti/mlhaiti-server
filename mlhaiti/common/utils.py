from django.utils.text import slugify

import django
import hashlib
import random
import string 


def NOW():
	return django.utils.timezone.localtime()

def create_code(instance,nb,new_hash=None,field="code"):
	_hash = hashlib.sha1(str(random.random()).encode()).hexdigest()[:nb]

	if new_hash is not None:
		_hash = new_hash
	else:
		_hash = hashlib.sha1(str(random.random()).encode()).hexdigest()[:nb]

	Klass = instance.__class__
	lookups = {field:_hash}
	qs_exists = Klass.objects.filter(**lookups).exists()
	if qs_exists:
		_hash = hashlib.sha1(str(random.random()).encode()).hexdigest()[:nb]
		return create_code(instance,_hash)
	return _hash

def create_slug(instance,new_slug=None,field_name="name"):
	def generator(size=10,chars=string.ascii_letters + string.digits):
		return ''.join(random.choice(chars) for _ in range(size))

	if new_slug is not None:
		slug = new_slug[:70]
	else:
		slug = slugify(getattr(instance,field_name))[:70] # params : Title or Name or Subject
		if not slug:
			slug = generator(10)

	Klass = instance.__class__
	qs_exists = Klass.objects.filter(slug=slug).exists()
	if qs_exists:
		new_slug = "%s-%s" % (slug,generator(4))
		if len(new_slug) > 60:
			new_slug = new_slug[:60]
		return create_slug(instance,new_slug,field_name)
	return slug
