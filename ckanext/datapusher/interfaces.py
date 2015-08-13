from ckan.plugins.interfaces import Interface


class IDataPusher(Interface):
    """
    The IDataPusher interface allows plugin authors to receive notifications
    before and after a resource is submitted to the datapusher service, as
    well as determining whether a resource should be submitted in can_upload

    The before_submit function, when implemented
    """

    def can_upload(self, resource_id):
        """ This call when implemented can be used to stop the processing of
        the datapusher submit function.  If this function returns False
        then processing will be aborted, whilst returning True will
        submit the resource to the datapusher service

        :param resource_id: The ID of the resource that is to be
            pushed to the datapusher service.

        Returns ``True`` if the job should be submitted and ``False`` if the job
        should be aborted

        :rtype: bool
        """
        return True


    def after_upload(self, resource_dict, package_dict):
        """ After a resource has been successfully upload to the datastore
        this method will be called with the ID of the resource that was
        uploaded.

        :param resource_id: The ID of the resource that was
            successfully uploaded to the datastore
        """
        pass
