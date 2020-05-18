from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from sports.serializer import NPEquipmentSerializer, NPSportInformationSerializer
from .models import *
from sports.models import NPEquipment
class NPAmenitiesSerializer(ModelSerializer):

    class Meta:
        model = NPAmenities
        fields = '__all__'

class VenueTimingsSerializer(ModelSerializer):
    day = serializers.SerializerMethodField()
    time_start = serializers.SerializerMethodField()
    time_end = serializers.SerializerMethodField()

    def get_day(self, obj):
        return obj.get_day_display()

    def get_time_start(self, obj):
        return obj.time_start.strftime("%I:%M%p")

    def get_time_end(self, obj):
        return obj.time_end.strftime("%I:%M%p")

    class Meta:
        model = VenueTimings
        fields = '__all__'

class VenueImagesSerializer(ModelSerializer):

    class Meta:
        model = VenueImages
        fields = '__all__'

class NPSpaceSerializer(ModelSerializer):

    class Meta:
        model = NPSpace
        fields = '__all__'

class NPCourtSerializer(ModelSerializer):

    class Meta:
        model = NPCourt
        fields = '__all__'

class NpVenueSerializer(ModelSerializer):
    venue_images = serializers.SerializerMethodField()
    venue_timing = serializers.SerializerMethodField()
    amenities = NPAmenitiesSerializer(many=True)
    venue_spaces = serializers.SerializerMethodField()
    venue_addon = serializers.SerializerMethodField()
    sport_info = serializers.SerializerMethodField()

    def get_venue_images(self, obj):#Here obj is venue object
        # venue_images = VenueImages.objects.filter(venue=obj)
        # return VenueImagesSerializer(venue_images, many=True).data
        return VenueImagesSerializer(obj.venueimages_set.all(), many=True).data

    def get_venue_timing(self, obj):
        return VenueTimingsSerializer(obj.venuetimings_set.all(), many=True).data

    def get_venue_spaces(self, obj):
        return NPSpaceSerializer(obj.npspace_set.all(), many=True).data

    def get_venue_addon(self, obj):
        addons = NPEquipment.objects.filter(sport__venue=obj)
        return NPEquipmentSerializer(addons, many=True).data

    def get_sport_info(self, obj):
        return NPSportInformationSerializer(obj.npsportinformation_set.all(), many=True).data

    class Meta:
        model = NPVenue
        fields = '__all__'